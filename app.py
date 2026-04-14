<<<<<<< HEAD
from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent = 4)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html",tasks=tasks)

@app.route("/add", methods =["POST"])

def add():
    name = request.form.get("task")
    priority = request.form.get("priority")
    due_date = request.form.get("due_date")

    tasks = load_tasks()
    tasks.append({
        "name": name,
        "done": False,
        "priority": priority,
        "due_date" : due_date
        })

    save_tasks(tasks)
    return redirect("/")

@app.route("/done/<int:task_id>")
def done(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
        save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect("/")

@app.route("/edit/<int:task_id>", methods = ["POST"])
def edit(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["name"] = request.form.get["task"]
        tasks[task_id]["priority"] = request.form.get["priority"]
        tasks[task_id]["due_date"] = request.form.get["due_date"]
        save_tasks(tasks)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug= True)


=======
from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent = 4)

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html",tasks=tasks)

@app.route("/add", methods =["POST"])

def add():
    name = request.form.get("task")
    priority = request.form.get("priority")
    due_date = request.form.get("due_date")

    tasks = load_tasks()
    tasks.append({
        "name": name,
        "done": False,
        "priority": priority,
        "due_date" : due_date
        })

    save_tasks(tasks)
    return redirect("/")

@app.route("/done/<int:task_id>")
def done(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
        save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect("/")

@app.route("/edit/<int:task_id>", methods = ["POST"])
def edit(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["name"] = request.form.get["task"]
        tasks[task_id]["priority"] = request.form.get["priority"]
        tasks[task_id]["due_date"] = request.form.get["due_date"]
        save_tasks(tasks)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug= True)


>>>>>>> 33630a6ffc41c011ce5dd44f5a801182c8575b4a
