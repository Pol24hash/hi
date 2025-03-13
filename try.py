from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "secretkey"

# User credentials
VALID_USERNAME = "irish"
VALID_DATE = "2004-03-17"  # Format: YYYY-MM-DD

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    selected_date = request.form['date']
    
    if username == VALID_USERNAME and selected_date == VALID_DATE:
        session['user'] = username
        return redirect(url_for('welcome'))
    else:
        flash("Invalid Credentials!", "danger")
        return redirect(url_for('login_page'))

@app.route('/welcome')
def welcome():
    if 'user' in session:
        return render_template('welcome.html', username=session['user'])
    else:
        return redirect(url_for('login_page'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)
