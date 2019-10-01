from app import app
from flask import render_template


@app.route('/legal')
def template():
    return render_template('home.html')
