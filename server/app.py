#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    parameter_list = f''
    for i in range(parameter):
        parameter_list += f'{i}\n'
    return parameter_list

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    if operation == '-':
        return str(num1 - num2)
    if operation == '*':
        return str(num1 * num2)
    if operation == 'div':
        return str(num1 / num2)
    if operation == '%':
        return str(num1 % num2)