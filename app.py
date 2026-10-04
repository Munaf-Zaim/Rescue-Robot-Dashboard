"""RESQ-AI dashboard server.
Run:  pip install flask   then   python app.py
Open: http://127.0.0.1:5000   (Web Bluetooth works on 127.0.0.1 in Chrome/Edge)
"""
from pathlib import Path
from flask import Flask, send_from_directory
 
BASE = Path(__file__).parent / "static"
app = Flask(__name__, static_folder=None)
 
 
@app.after_request
def no_cache(resp):
    # always load the newest dashboard file, never an old cached copy
    resp.headers["Cache-Control"] = "no-store, max-age=0"
    return resp
 
 
@app.route("/")
def index():
    return send_from_directory(BASE, "index.html")
 
 
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
