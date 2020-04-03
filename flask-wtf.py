from flask import Flask, redirect, render_template, request
from random import choice
import json

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


professions = ['инженер-исследователь',
               'пилот', 'строитель', 'экзобиолог',
               'врач', 'инженер по терраформированию',
               'климатолог', 'специалист по радиационной защите',
               'астрогеолог', 'гляциолог, инженер жизнеобеспечения',
               'метеоролог', 'оператор марсохода', 'киберинженер',
               'штурман', 'пилот дронов']


@app.route('/list_prof/<list>')
def prof(list):
    return render_template('index.html', list_=list, user_list=professions)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/answer/<title>/<surname>/<name>/<education>/<profession>/<sex>/<motivation>/<ready>')
def ready(title, surname, name, education, profession, sex, motivation, ready):
    param = {}
    param['title'] = title
    param['surname'] = surname
    param['name'] = name
    param['education'] = education
    param['profession'] = profession
    param['sex'] = sex
    param['motivation'] = motivation
    param['ready'] = ready
    return render_template('auto_answer.html', **param)


@app.route('/auto_answer')
def ready_2():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = 'Watny'
    param['name'] = 'Mark'
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман марсохода'
    param['sex'] = 'male'
    param['motivation'] = 'Всегда мечтал застрять на Марсе'
    param['ready'] = 'Да'
    return render_template('auto_answer.html', **param)


people = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капуо', 'Тедди Сандерс', 'Шон Бин']


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', people=people)


@app.route('/table/<sex>/<int:age>')
def table(sex, age):
    return render_template('table.html', sex=sex, age=age)


images = ['/static/img/mars1.jpg', '/static/img/mars2.jpeg', '/static/img/mars3.jpeg']
@app.route('/galery', methods=['POST', 'GET'])
def galery():
    new = f'/static/img/mars{len(images) + 1}.jpg'
    if request.method == 'GET':
        return render_template('galery.html', images=images)
    elif request.method == 'POST':
        f = request.files['file']
        with open(new.lstrip('/'), "wb") as file:
            file.write(f.read())
        images.append(new)
        return render_template('galery.html', images=images)


@app.route('/member')
def member():
    data = open('templates/people.json')
    a = data.readlines()
    data.close()
    data = json.loads(''.join(a))
    member = data['Members'][choice(range(5))]
    return render_template('member.html', member=member, work=', '.join(sorted(member['work'])))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
