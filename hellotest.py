from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("aboutUs.html")

@app.route('/john')
def John():
    return "<h1>Hello John</h1>" 

@app.route('/welcome/<name>')
def Welcome_name(name):
    return 'Welcome ' + name + '!'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

