from flask import Flask
app = Flask(__name__)

@app.route("/hi")
def hello2():
    return "Hi!!!"

@app.route("/")
def hello():
    return "Main page"
