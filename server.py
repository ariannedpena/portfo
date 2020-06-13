from flask import Flask, render_template, request, redirect

app = Flask(__name__)
from datetime import datetime
import csv


@app.route('/')
def html_index():
	return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


def write_to_file(data):
	with open('./database.txt', mode='a') as database:
		now = datetime.now()
		email = data['email']
		subject = data['subject']
		message = data['message']
		datetime1 = now

		file = database.write(f'\n{email},{subject},{message},{datetime1}')


def write_to_csv(data):
	with open('./database.csv', mode='a', newline='') as database2:
		now = datetime.now()
		email = data['email']
		subject = data['subject']
		message = data['message']
		datetime1 = now

		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message, datetime1])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			print(data)
			write_to_file(data)
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'Did not save to database! Please try again'
	else:
		return 'Something went wrong, Please try again.'
