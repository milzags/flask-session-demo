from flask import Flask, render_template, request, session, redirect, flash
from flas_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/secret-invite')
def show_secret_inite():
    if session.get('entered-pin', False)
        return render_template('invite.html')
    else
        return redirect('/login')

@app.route('/login-form')
def show_login_form():
    return render_template('login-form.html')

@app.route('/login')
def verify_secret_code():
    SECRET = 'chickenz_are_gr8'
    secretcode = request.args['secret_code']
    if SECRET == secretcode:
        session['entered-pin'] = True
        return redirect('/secret-invite')
    else:
        flash('You need to enter the correct pin to access details')
        return redirect('login-form')