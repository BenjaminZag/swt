from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "homepage geht"

if __name__ == __name__:
    app.run()