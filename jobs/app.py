from flask import flask, render_function

app = Flask(__name__)

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_function('index.html')

# if __name__ == "__main__":
#     app.run()