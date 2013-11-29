from textprocess.preprocessor import preprocess
from flask import *
import datetime


app = Flask(__name__)
app.secret_key = 'shivam bansal'

@app.route('/',methods=['GET','POST'])
def index():
	error = None 
	if request.method == 'POST':
		if request.form['string'] == "":
			flash("string is empty")
		else:
			return redirect(url_for('api', variable = request.form['string']))
	return render_template('index.html')

@app.route('/api')
def api():
	input1 = request.args['variable']

	data = preprocess(str(input1))
	output = {}
	output['date'] = datetime.datetime.now().strftime("%d/%m/%Y")
	output['response'] = data
	output['message'] = "Thanks For Using Text Process"
	return jsonify(**output)


if __name__ == '__main__' :
	app.run(debug=True)

