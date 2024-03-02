from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/answer")
@app.route("/auto_answer")
def requi():
    params = {}
    params['title'] = 'Загатовка'
    params['surname'] = "Watny"
    params['name'] = 'Mark'
    params['education'] = 'выше среднего'
    params['professoin'] = 'штурман марсхода'
    params['sex'] = 'male'
    params['motivation'] = 'Всегда мечтал застрять на Марсе!'
    params['ready'] = 'True'
    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')