from flask import Flask,render_template,request,redirect

app = Flask(__name__)
messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=messages)
    

@app.route('/send', methods=['POST'])
def send():
    skill = request.form.get('skill')

    messages.append(skill)

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)