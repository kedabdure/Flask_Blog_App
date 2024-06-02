from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '87008de58453f89f1af43456cc8bdf00'


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

# @app.route("/register")
# def register():
#     form = RegistrationForm()
#     return render_template('register.html', title='Register', form=form)

# @app.route("/login")
# def register():
#     form = RegistrationForm()
#     return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
    app.run(debug=True)