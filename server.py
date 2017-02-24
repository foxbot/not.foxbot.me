from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<image>')
def hello_world(image):
	return render_template('image.html', image=image)

if __name__ == '__main__':
	app.run(port=3820)