from flask import Flask
import os
import markdown

app = Flask(__name__)

MD_FOLDER = "files"

@app.route("/")
def home():
    files = [f for f in os.listdir(MD_FOLDER) if f.endswith(".md")]

    html = "<h1>Markdown Files</h1><ul>"

    for file in files:
        html += f'<li><a href="/view/{file}">{file}</a></li>'

    html += "</ul>"

    return html


@app.route("/view/<filename>")
def view(filename):
    path = os.path.join(MD_FOLDER, filename)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    return markdown.markdown(content)


app.run(host="0.0.0.0", port=8000)