from flask import Flask, render_template, request
from wtforms import Form, StringField, PasswordField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Login logic
        return 'Login successful'
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- login.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            height: 40px;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        button[type="submit"] {
            width: 100%;
            height: 40px;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button[type="submit"]:hover {
            background-color: #3e8e41;
        }
    </style>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <label for="username">Username:</label>
        {{ form.username(size=32) }}
        <label for="password">Password:</label>
        {{ form.password(size=32) }}
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

```html
<!-- accessibility.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            height: 40px;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        button[type="submit"] {
            width: 100%;
            height: 40px;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button[type="submit"]:hover {
            background-color: #3e8e41;
        }
        /* Accessibility styles */
        .screen-reader-text {
            position: absolute;
            clip: rect(1px, 1px, 1px, 1px);
            padding: 0;
            border: 0;
            height: 1px;
            width: 1px;
            overflow: hidden;
        }
        .screen-reader-text:focus {
            clip: auto;
            height: auto;
            margin: -1px;
            overflow: visible;
            padding: 0;
            position: static;
            width: auto;
            white-space: normal;
        }
    </style>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        <label for="username">Username:</label>
        {{ form.username(size=32) }}
        <span class="screen-reader-text">Username field</span>
        <label for="password">Password:</label>
        {{ form.password(size=32) }}
        <span class="screen-reader-text">Password field</span>
        <button type="submit">Login</button>
        <span class="screen-reader-text">Submit button</span>
    </form>
</body>
</html>
```

```python
from flask import Flask, render_template, request
from wtforms import Form, StringField, PasswordField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

@app.route('/accessibility', methods=['GET', 'POST'])
def login_accessibility():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Login logic
        return 'Login successful'
    return render_template('accessibility.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
