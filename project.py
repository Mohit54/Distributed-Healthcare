from flask import Flask, render_template, request
from flask import Flask, redirect, url_for, render_template, request, abort
from werkzeug.utils import secure_filename
import os
from flask import Flask
from flask import request, jsonify, send_from_directory
import traceback
# Initialize the Flask application
import random
import string
from flask import Flask
from flask import request, jsonify, send_from_directory
import traceback

app = Flask(__name__,template_folder='./',static_url_path='/static')
UPLOAD_FOLDER ='./uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "success", "message": "Server is running"})


# route http posts to this method
@app.route('/home')
def test():
    return render_template('index.html')
@app.route('/about')
def test_about():
    return render_template('about.html')

app.run(host="0.0.0.0", port=5000,debug=True,use_reloader=False)