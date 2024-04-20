#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
import subprocess


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """This function executes when 0.0.0.0:/5000/states_list
    is requested
    """
    state_list = storage.all("State")
    states = []
    for value in state_list.values():
        states.append(value)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down_context(exception):
    """This function removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    subprocess.run("export", "FLASK_APP=7-states_list.py")
    subprocess.run("flask run")
