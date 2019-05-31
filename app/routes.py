from app import app
from flask import render_template
from app.parser import getPoem
from app.data import getStats


@app.route('/')
@app.route('/index')
def index():
    url = 'http://www.arthurleej.com/e-love.html'
    response = getPoem(url)

    return render_template('index.html', response=response)

@app.route('/dataframe')
def dataFrame():
    response = getStats()
    return render_template('dataframe.html', response=response)
