from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    print(f"the current count is {session['count']}")
    return render_template("index.html", count=session['count'])

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add')
def add_two():
    session['count'] += 1
    print('the add function is running')
    print('*'*50)
    print(f"the current session count is {session['count']}")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)