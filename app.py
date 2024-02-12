from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobListings = [
  { 
    "id" : 1,
    "title" : "Data Analyst",
    "location" : "Gurgaon, India",
    "salary" : "Rs. 10,00,000"
  },{ 
    "id" : 2,
    "title" : "Data Scientist",
    "location" : "Pune, India",
    "salary" : "Rs. 12,00,000"
  },
  { 
    "id" : 3,
    "title" : "Frontend Engineer",
    "location" : "Mumbai, India",
    "salary" : "Rs. 15,00,000"
  },{ 
    "id" : 4,
    "title" : "Backend Engineer",
    "location" : "Mumbai, India",
    "salary" : "Rs. 18,00,000"
  },
  { 
    "id" : 5,
    "title" : "Quality Analyst",
    "location" : "Gurgaon, India",
    # "salary" : "Rs. 8,00,000"
  },
]

@app.route("/")
def hello():
  return render_template("home.html", jobs=jobListings)

@app.route("/api/jobs")
def getJobs():
  return jsonify(jobListings)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
