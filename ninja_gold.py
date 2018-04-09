from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "key"

@app.route('/')
def index():
    session["gold"] = 0
    session["activity"] = 0
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process_money():
    building_input = request.form["building"]
    if building_input == "farm":
        earnings = random.randrange(10, 20)
        print "farm"
        print earnings
        session["activity"].append("Earned " + str(earnings) + " gold from the farm!")
    elif building_input == 'cave':
        earnings = random.randrange(5, 10)
        print 'cave'
        print earnings
    elif building_input == 'house':
        earnings = random.randrange(2, 5)
        print 'house'
        print earnings
    elif building_input == 'casino':
        earnings = random.randrange(-50, 50)
        print 'casino'
        print earnings
    return redirect('/')

app.run(debug=True)