from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    flag = 0
    if number_1 is not None or number_2 is not None:
        if number_1.isnumeric() and number_2.isnumeric():
            number_1 = float(number_1)
            number_2 = float(number_2)
            flag = 1
    operation = request.form.get('operation')
    if flag == 0:
        flash(f'Invalid Input')
        return render_template('index.html')

    result = 0
    if operation == 'add':
        result = requests.get('http://addition:5001/add/'+str(number_1) +'/'+str(number_2)).text
    elif operation == 'minus':
        result =  requests.get('http://subtraction:5002/sub/'+str(number_1) +'/'+str(number_2)).text
    elif operation == 'multiply':
        result = requests.get('http://multiplication:5003/mul/'+str(number_1) +'/'+str(number_2)).text
    elif operation == 'divide':
        result = requests.get('http://division:5004/div/'+str(number_1) +'/'+str(number_2)).text
    elif operation=='gcd':
        result=requests.get('http://gcd:5005/gcd/'+str(number_1) +'/'+str(number_2)).text
    elif operation=='mod':
        result=requests.get('http://modulus:5006/mod/'+str(number_1) +'/'+str(number_2)).text
    elif operation=='equal':
        result=requests.get('http://equal:5007/equal/'+str(number_1) +'/'+str(number_2)).text
    if flag == 0:
        result = ""
    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
