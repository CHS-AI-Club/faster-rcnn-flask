from app import app
from flask import render_template, request, redirect
from app.detection import detect

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/post_image', methods=['POST', 'GET'])
def post_image():
    if request.method == 'POST':
        image_file = request.files.get('image-file', '')
        image = detect(image_file)
        return render_template('display.html', image=image)
    else:
        return render_template('index.html')
