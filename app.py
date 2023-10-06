# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Laetitia" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage

@app.route('/father')
def father():
    father_name = "Tishi"
    father_age = 36  # Replace with your father's age
    return render_template('father.html', name=father_name, age=father_age)

# define the route to mother webpage

@app.route('/mother')
def mother():
    mother_name = "Teena"
    mother_age = 42  # Replace with your mother's age
    return render_template('mother.html', name=mother_name, age=mother_age)


# define the route to friends webpage

@app.route('/brother')
def brother():
    brother_name = "Jonathan"
    brother_age = 12  # Replace with your friend's age
    return render_template('friend.html', name=brother_name, age=brother_age)



# add other routes, if you want





# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
