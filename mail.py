from flask import Flask
from flask_mail import Mail, Message

# https://prettyprinted.com/courses/the-flask-extensions-course/lectures/3043371
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'python3flask@gmail.com'
app.config['MAIL_PASSWORD'] = '9995797444n'
# app.config['MAIL_DEFAULT_SENDER'] = 'python3flask@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = ('My test mail', 'python3flask@gmail.com')
app.config['MAIL_MAX_EMAILS'] = None
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False


mail = Mail(app)
# or
# mail =Mail()
# mail.init_app(app)

@app.route('/')
def index():
    msg = Message('Hey There', recipients=['noufal@scientiaindia.com'])
    # add another mail
    # msg.add_recipient('new@mail.com')
    # Add body
    # msg.body = 'This is the message from noufal\'s app '
    msg.html = '<b>This is the message from noufal\'s app</b>'

    with app.open_resource('logo.jpg') as cat:
        msg.attach('cat.jpeg','image/jpeg', cat.read())
    mail.send(msg)
    return 'success'

@app.route('/bulk')
def bulk():
    users = [{'name' : 'Noufal', 'email':'noufal@scientiaindia.com' }]
    with mail.connect() as conn:
        for user in users:
            msg = Message('Bulk', recipients=[user['email']])
            msg.body = 'This is the message from noufal\'s app '
            conn.send(msg)


if __name__ == '__main__':
    app.run()
