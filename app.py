from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration
USERS = [
    {'email': 'user1@example.com', 'password': 'password1'},
    {'email': 'user2@example.com', 'password': 'password2'}
]

# Dummy job data for demonstration
JOBS = [
    {'title': 'Data Analyst', 'location': 'Wroclaw, Poland', 'salary': 'PLN 35,000'},
    {'title': 'Data Scientist', 'location': 'Poznan, Poland', 'salary': 'PLN 27,000'},
    {'title': 'Frontend Engineer', 'location': 'Remote'},
    {'title': 'Backend Engineer', 'location': 'San Francisco, USA', 'salary': '$150,000'}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        for user in USERS:
            if user["email"] == email and user["password"] == password:
                # Successful login, you can redirect to a dashboard or profile page
                return redirect(url_for("dashboard"))
        # If login fails, you can render an error message or redirect to the registration page
        return render_template("login.html", error="Invalid email or password")
    return render_template("login.html", error=None)

@app.route("/dashboard")
def dashboard():
    # You can render the dashboard page for authenticated users here
    return render_template("dashboard.html")

@app.route("/search")
def search_jobs():
    return render_template("job_list.html", jobs=JOBS)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Handle registration logic here
        # For example, add the new user to your USERS list
        email = request.form.get("email")
        password = request.form.get("password")
        USERS.append({'email': email, 'password': password})
        # Redirect to the login page after successful registration
        return redirect(url_for("login"))
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
