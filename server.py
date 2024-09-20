from flask import Flask, render_template, request
from testdata import generate_test
from waitress import serve
app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test')
def get_weather():
    numberoftests = request.args.get('numberoftests')
    regex = request.args.get('regex')
    print(numberoftests)
    print(regex)
    # Check for empty strings or string with only
    # spaces
    result = []
    for i in range(int(numberoftests)):
        result.append(generate_test(regex))
    return render_template(
        "test.html",
        results=result,
    )
    # City is not found by AP

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
