import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = open("index.html", "r", encoding="utf-8").read()
    return render_template_string(html)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
