from flask import Flask
import random

app = Flask(__name__)
instance = random.randint(0, 100)


@app.route("/")
def hello():
    return "Hello World from %d!\n" % instance
