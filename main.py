from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
       <form action="/" method="post">
            <label for="rot"><b>Rotate by:</b></label>
            <input id="rot" type="text" name="rot" />
                </br>
            <textarea id="text" name="text" rows="5">{0}</textarea>
                </br>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")

@app.route('/', methods=['POST'])
def encrypt():
    rotated = ''
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    rotated = rotate_string(text, rot)
    return form.format(rotated) 

app.run()
