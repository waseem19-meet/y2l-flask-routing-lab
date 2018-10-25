from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop')
def shop_page():
	items = {"T-shirts":'50',
			"Pants":30,
			"Shoes":45,
			"Skirts":27}
	return render_template( "shop.html",
		items=items)

if __name__ == '__main__':
   app.run(debug = True)