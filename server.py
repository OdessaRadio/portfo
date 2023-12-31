from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/") 
def home():
    return render_template('index.html') 

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET']) # GET - browser wants us to send info, POST - browser wants us to save info
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(f"dat: {data}")
            write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not saving to DB'
    else:
        return 'try again'

def write_to_file(data):
    with open('database.txt', mode = 'a') as db:
        email   = data['email']
        subject = data['subject']
        message = data['message']
        file = db.writelines(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode = 'a', newline='') as db2:
        email   = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(db2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

#@app.route("/index.html") 
#def my_home():
#    return render_template('index.html') 

#@app.route("/works.html")
#def works():
#    return render_template('works.html')
#
#@app.route("/about.html")
#def about():
#    return render_template('about.html')
#
#@app.route("/contact.html")
#def contact():
#    return render_template('contact.html')
#
#@app.route("/components.html")
#def components():
#    return render_template('components.html')




