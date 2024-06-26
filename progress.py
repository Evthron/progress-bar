import os

from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY", "secret_l801#+#a&^1mz)_p&qyq51j51@20_74c-xi%&i)b*u_dt^2=2key"
)


def get_progress_color(progress, scale):
    ratio = progress / scale

    if ratio < 0.3:
        return "#d9534f" #red
    elif ratio < 0.7:
        return "#f0ad4e" #orange
    else:
        return "#5cb85c" #green


def get_template_fields(progress):
    title = request.args.get("title")

    try:
        scale = int(request.args.get("scale"))
    except (TypeError, ValueError):
        scale = 100

    # Special use of conditional
    progress_width = 60 if title else 90
    try:
        progress_width = int(request.args.get("width"))
    except (TypeError, ValueError):
        pass
 
    return {
        "title": title,
        "title_width": 10 + 6 * len(title) if title else 0,
        "title_color": request.args.get("color", "428bca"),
        "scale": scale,
        "progress": progress,
        "progress_width": progress_width,
        "progress_color": get_progress_color(progress, scale),
        "suffix": request.args.get("suffix", "%"),
    }


@app.route("/<int:progress>/")
def get_progress_svg(progress):
    template_fields = get_template_fields(progress)
    return render_template("progress.svg", **template_fields)


@app.route("/")
def redirect_to_github():
    return redirect("http://127.0.0.1:5000/50")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port)
