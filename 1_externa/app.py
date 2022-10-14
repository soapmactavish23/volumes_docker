import flask
from flask import request, json, jsonify
import requests

app = flash.Flash(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def index():
    data = request.get('https://randomuser.me/api')
    return data.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")