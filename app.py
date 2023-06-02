from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/JackRC')
def JackRC():
	return render_template('JackRC.html')

@app.route('/IIJohnN')
def IIJohnN():
	return render_template('IIJohnN.html')

@app.route('/JohnC')
def JohnC():
    return render_template('JohnC.html')


@app.route('/skylee')
def skylee():
	return render_template('skylee.html')


@app.route('/Paul')
def Paul():
	return render_template('Paul.html')

@app.route('/Jacob')
def Jacob():
	return render_template('Jacob.html')

@app.route('/JacobII')
def JacobII():
	return render_template('JacobII.html')

@app.route('/JohnN')
def JohnN():
    	return render_template('JohnN.html')

@app.route('/Spencer')
def Spencer():
    	return render_template('Spencer.html')


@app.route('/Maddix')
def Maddix():
	return render_template('maddix.html')

@app.route('/Jakobi')
def Jakobi(): 
	return render_template('jakobi.html')

@app.route('/Peyton')
def Peyton(): 
	return render_template('Peyton.html')
