from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
app.config.from_pyfile('config.cfg')


@app.route('/')
def index():
    return redirect(url_for('points_table'))


@app.route('/points-table')
def points_table():
    return render_template('points-table.html')


@app.route('/predictions')
def predictions():
    return render_template('predictions.html')


if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"])
