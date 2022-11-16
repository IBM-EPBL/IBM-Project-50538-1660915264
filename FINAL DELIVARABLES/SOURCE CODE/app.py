from flask import Flask,render_template

app = Flask(_name_)

@app.route('/Chatbot', methods = ['GET','POST'])

def Chatbot():
    return render_template('Chatbot.html')

if _name_ == '_main_':
 app.run()