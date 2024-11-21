# app.py

from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app instance
app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return """
    <h1>Welcome to My App</h1>
    <p>This is a simple Flask app. Navigate to /form to submit some data.</p>
    """

# Form route to display a form
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_name = request.form['name']
        user_message = request.form['message']
        return redirect(url_for('result', name=user_name, message=user_message))
    return """
    <h1>Submit Your Info</h1>
    <form method="post" action="/form">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br>
        <button type="submit">Submit</button>
    </form>
    """

# Result route to display the submitted data
@app.route('/result')
def result():
    name = request.args.get('name')
    message = request.args.get('message')
    return f"""
    <h1>Thank You, {name}!</h1>
    <p>Your message: {message}</p>
    <a href="/">Go Back Home</a>
    """

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
