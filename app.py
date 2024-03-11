from flask import Flask, render_template

app = Flask(__name__)


@app.route('/base/')
def base():
    return render_template('base.html')


@app.route('/main/')
def main():
    context = {'title': 'Главная/nbngha'}
    return render_template('main.html', **context)

@app.route('/dress/')
def dress():
    context = {'title': 'Одежда/'}
    return render_template('dress.html', **context)




if __name__ == '__main__':
    app.run()
