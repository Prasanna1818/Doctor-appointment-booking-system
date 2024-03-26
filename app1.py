from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
conn=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="prasanna2410",
    database="appointments"
)
c=conn.cursor()
@app.route("/")
def hi():
    return render_template("homepage.html")

@app.route("/book")
def form():
    return render_template("formpage.html")

@app.route("/doctor")
def format():
    return render_template("extra.html")

@app.route("/http",methods=['POST', 'GET'])
def http():
    if request.method == 'POST':
        name = request.form['Name']
        age = request.form['Age']
        timeslot=request.form['Timeslot']
        department=request.form['Department']
        c.execute("INSERT INTO data(name,age,timeslot,department)VALUES(%s,%s,%s,%s)",
                  (name,age,timeslot,department))
        conn.commit()
    return render_template("done.html")

@app.route('/view', methods=['GET', 'POST'])
def view():
        if request.method == 'POST':
            name = request.form['name']
        name=name
        c.execute("select * from data where name = %s;",(name,))
        appointments = c.fetchall()
        return render_template('search.html', appointments=appointments)

@app.route('/extra', methods=['GET', 'POST'])
def extra():
     return render_template('extra.html')

@app.route('/search', methods=['Get','POST'])
def search():
    return render_template("details.html")
     

if __name__=="__main__":
    app.run(debug=True)