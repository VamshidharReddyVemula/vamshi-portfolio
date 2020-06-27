#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:00:09 2020

@author: vemulas
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')

def home():
    return render_template("index1.html")

@app.route('/vvr/')
def about():
    return "About of vamshi"


if __name__ == "__main__":
    app.run(debug = True)
