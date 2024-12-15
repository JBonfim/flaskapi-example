from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content="Testing", x=4)


@app.route("/")
def home():
    return render_template("index.html", content={"a":2, "b":"hello"})

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"