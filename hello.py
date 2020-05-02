from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Post1998@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# this would link an instance of a database that we can interact with in SQLAlchemy land to our Flask app. 
db = SQLAlchemy(app)
# db is an instance of database and offers certain objects like db.Model, db.session
# db.Model ability to create and manipulate models
# db.session ability to create and manipulate transactions



class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    # __repr__(optional)  ability to customnize a printable string (useful for debugging)
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'
# db.create_all() detects models and creates tables for them (if they don't exist)
db.create_all()

@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name

if __name__ == "__main__":
    app.run(debug=True)


    