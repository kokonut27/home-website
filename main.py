from flask import Flask, render_template
import os, time, requests, json
import REPLAPI as repl #Maybe remove?


cycles = repl.replit_cycles("JBloves27")
bio = repl.replit_bio("JBloves27")
langs1 = repl.replit_langs("JBloves27")
langs = langs1[0].capitalize() + ", " + langs1[1].capitalize() + ", " + langs1[2].capitalize()

os.system("clear")

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def index():
  return render_template(
    "index.html",
    replitname = "JBloves27",
    replitcycles = cycles,
    replitbio = bio,
    replitlangs = langs,
  )

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

app.run(host="0.0.0.0",port=8080)

#CREDITS TO CODEPEN FOR NAVBAR.