from flask import Flask, request
from flask import render_template
from flask import current_app as app
import application.models as md


@app.route("/", methods=["GET", "POST"])
def students():
    students = md.Student.query.all()
    return render_template("index.html", students=students)


@app.route("/student/create", methods=['GET', 'POST'])
def create_student():
    return render_template("add_student.html")
