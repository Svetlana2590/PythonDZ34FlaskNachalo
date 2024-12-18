from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    employees = [
        {'name': 'Василий', 'position': 'Инженер'},
        {'name': 'Анна', 'position': 'Врач'},
        {'name': 'Екатерина', 'position': 'Маркетолог'},
    ]
    return render_template('index.html', name=name, employees=employees)


if __name__ == '__main__':
    app.run(debug=True)






