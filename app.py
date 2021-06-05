from flask import Flask, render_template, request, url_for, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'burdeniuk.flask.email@gmail.com'
app.config['MAIL_PASSWORD'] = 'burdeniukflask'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods = ["POST", "GET"])
def contact():
    if request.method == "POST":
        user = request.form["name"]
        user_mail = request.form["mail"]
        user_text = request.form["form_text"]

        msg = Message('Hello', sender=user_mail,
                      recipients=['mr.burdeniuk@gmail.com'])
        msg.body = f"Hello Flask message sent from Flask-Mail \n " \
                   f"Send from: {user_mail} \n" \
                   f"Name: {user} \n" \
                   f"\n Text message: {user_text}"
        mail.send(msg)

        return redirect(url_for('user', usr = user))
    else:
        return render_template('contact.html')



@app.route('/<usr>')
def user(usr):

    return f'<h1>Your message is sended, {usr}!</h1> <br/> <a href="/">Back to webpage...</a>'


@app.route('/bomber', methods = ["POST", "GET"])
def bomb():
    if request.method == "POST":
        for i in range(15):
            text_bomb = request.form["bomber_text"]
            mail_bomb = request.form["mail_bomb"]

            msg = Message('Hello', sender='nekitdoter@gmail.com',
                          recipients=[mail_bomb])
            msg.body = f"It is {i+1} message '{text_bomb}'"

            mail.send(msg)

        return "<h1>Ready....</h1> <a href = '/'>Back to site</a>"
    else:
        return render_template('bomber_mail.html')


if __name__ == '__main__':
    app.run(debug=True)
