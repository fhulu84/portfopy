from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)#__name__ == __main__ bcs we run this app in our main file

#INIT CSV File Headers
with open('./database.csv', 'a', newline='') as db:
  csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  csv_writer.writerow(['Email', 'Subject', 'Message'])

def write_to_db_txt(data): 
  with open('./database.txt', 'a') as db:
    email = data['email']
    subject = data['subject']
    message = data['message']
    file = db.write(f'{email},{subject},{message}\n')

def write_to_db_csv(data):
  with open('./database.csv', 'a', newline='') as db:
    email = data['email']
    subject = data['subject']
    message = data['message']
    csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email, subject, message])
    # With DictWriter
    # csv_writer = csv.DictWriter(db, fieldnames=['email', 'subject', 'message'])
    # csv_writer.writerow(data)
  
@app.route('/')
def my_home():
  return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
  return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
    try:
      data = request.form.to_dict()
      write_to_db_csv(data)
      return redirect('/thankyou.html')
    except:
      return 'did not save to database'
    
  else:
    return 'something went wrong. try again!'
