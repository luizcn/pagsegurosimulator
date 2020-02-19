from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja2')

@app.route('/divide_form')
def divide_form():
    return render_template('divide_form.jinja2')

@app.route('/divide_result', methods=['POST'])
def divide_result():
    number = float(request.form['number'])
    fixTax = 0.40
    taxNum = number + fixTax
    result = taxNum * 1.0415585
    return render_template('divide_result.jinja2',
    number=number, 
    result=round(result, 2),
    result2=round((result * 1.0451), 2),
    result3=round((result * 1.0604), 2),
    result4=round((result * 1.0759), 2),
    result5=round((result * 1.0915), 2),
    result6=round((result * 1.1072), 2),
    result7=round((result * 1.1231), 2),
    result8=round((result * 1.1392), 2),
    result9=round((result * 1.1554), 2),
    result10=round((result * 1.1717), 2),
    result11=round((result * 1.1882), 2),
    result12=round((result * 1.2048), 2),
    presult2=round((result * 1.0451) / 2,2),
    presult3=round((result * 1.0604) / 3,2),
    presult4=round((result * 1.0759) / 4,2),
    presult5=round((result * 1.0915) / 5,2),
    presult6=round((result * 1.1072) / 6,2),
    presult7=round((result * 1.1231) / 7,2),
    presult8=round((result * 1.1392) / 8,2),
    presult9=round((result * 1.1554) / 9,2),
    presult10=round((result * 1.1717) / 10,2),
    presult11=round((result * 1.1882) / 11,2),
    presult12=round((result * 1.2048) / 12,2))
    

if __name__ == '__main__':
    app.debug = True
    app.run()