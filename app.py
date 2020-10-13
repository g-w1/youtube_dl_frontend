from flask import Flask, render_template, request, send_from_directory
import os
import validators

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    print(request)
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        vidurl = request.form["url"]
        name_of_vid = request.form["name"]
        if not validators.url(vidurl):
            return "<h1>URL NOT VALID</h1>"
        else:
            os.system(f"youtube-dl  {vidurl} -o vids/{name_of_vid}.mp4")
            return f"<h1><a href='/vids/{name_of_vid}.mp4'>{name_of_vid}</a><h1>"


@app.route("/vids/<path:path>")
def send_file(path):
    return send_from_directory("vids", path)


if __name__ == "__main__":
    app.run()
