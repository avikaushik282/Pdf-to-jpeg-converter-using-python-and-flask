from flask import Flask , render_template , jsonify
from flask.globals import request
from pdf2image import convert_from_path
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/conver')
def pdf2image():
    sr = str(request.args.get('sc'))
    ds = str(request.args.get('des'))

    try:
        images = convert_from_path(sr,poppler_path='./poppler-0.68.0/bin',size=(9020,9020))
        f = sr.split('\\')[-1].split('.')[0]

        for i, image in enumerate(images):
            image.save(f'{ds}/{f}-{i}.jpeg','JPEG')

        d = { f"{f}-{i}.jpeg" : f'{ds}/{f}-{i}.jpeg' for i in range(len(images))}

        return jsonify(d)

    except Exception as e:
        return render_template('index.html', text=f"No pdf found")


if __name__=="__main__":
    app.run(debug=True)