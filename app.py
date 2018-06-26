import requests
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from config import Configuration

# My 23 microservice!
# My first # microservice!


# create Flask app
app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

# GET request to ip.jsontest.com
def home():
    return render_template('home.html')

def rest_request_example():
    print (requests.get("http://140.86.15.104:3000/shield/45/0/pink/OraLevchenko").text)
print (requests.get("http://140.86.15.104:3000/shield/45/1/pink/OraLevchenko").text)
print (requests.get("http://140.86.15.104:3000/shield/45/2/pink/OraLevchenko").text)
print (requests.get("http://140.86.15.104:3000/shield/45/3/pink/OraLevchenko").text)
print (requests.get("http://140.86.15.104:3000/shield/45/4/pink/OraLevchenko").text)
print (requests.get("http://140.86.15.104:3000/shield/45/5/pink/OraLevchenko").text)
print (requests.get("http://140.86.15.104:3000/shield/45/6/pink/OraLevchenko").text)
print (requests.get("http://140.86.15.104:3000/shield/45/7/pink/OraLevchenko").text)
print (requests.get("http://140.86.15.104:3000/shield/45/8/pink/OraLevchenko").text)
print (requests.get("http://140.86.15.104:3000/shield/45/9/pink/OraLevchenko").text)

def read_db_SQL_example():
    conn = db.get_engine().connect()
    sql = "SELECT * FROM SampleTable"
    results = conn.execute(sql)
    rows = ""
    for row in results:
        rows = rows + ','.join(row) + "<br/>"
    print(rows)
	 
rest_request_example()
try:
	read_db_SQL_example()
except:
	print ('Could not connect to database')
	
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
