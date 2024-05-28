from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Route for serving the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Example routes for other endpoints
@app.route('/about')
def about():
    return "This is the about page."

@app.route('/projects')
def projects():
    return "This is the projects page."

# Route to serve project data as JSON
@app.route('/api/projects')
def get_projects():
    projects = [
        {
            "title": "Robotics Project",
            "description": "Built an autonomous robot using Arduino and various sensors.",
            "image": "images/robotics.png",
            "github": "https://github.com/yourusername/robotics-project",
            "liveDemo": "https://yourlivedemo.com/robotics",
            "width": 300,
            "height": 200
        },
        {
            "title": "Solar-Powered System",
            "description": "Designed an efficient solar-powered system for residential use.",
            "image": "images/solar.png",
            "github": "https://github.com/yourusername/solar-project",
            "liveDemo": "https://yourlivedemo.com/solar",
            "width": 300,
            "height": 200
        },
        {
            "title": "Software Development",
            "description": "Developed a full-stack web application using React and Node.js.",
            "image": "images/software.png",
            "github": "https://github.com/yourusername/software-project",
            "liveDemo": "https://yourlivedemo.com/software",
            "width": 300,
            "height": 200
        }
    ]
    return jsonify(projects)

@app.route('/contact', methods=['POST'])
def contact():
    # Handle contact form submission
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # You can process the message here (e.g., send email)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
