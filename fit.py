from flask import Flask, render_template_string, request

app = Flask(__name__)

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fitness Hub</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
            color: #333;
            scroll-behavior: smooth;
        }
        header {
            background: #ff6a6a;
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        header h1 {
            margin: 0;
        }
        nav ul {
            list-style: none;
            display: flex;
            gap: 1rem;
            margin: 0;
            padding: 0;
        }
        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        section {
            padding: 2rem;
            margin: 2rem auto;
            max-width: 800px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #ff6a6a;
            text-align: center;
        }
        .interactive {
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .interactive:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        form input {
            padding: 0.5rem;
            font-size: 1rem;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        form button {
            padding: 0.7rem;
            font-size: 1rem;
            background: #ff6a6a;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background 0.3s;
        }
        form button:hover {
            background: #e55d5d;
        }
        #bmi-result {
            font-weight: bold;
            text-align: center;
            margin-top: 1rem;
        }
        footer {
            text-align: center;
            padding: 1rem;
            background: #333;
            color: white;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>Fitness Hub</h1>
        <nav>
            <ul>
                <li><a href="#exercises">Exercises</a></li>
                <li><a href="#nutrition">Nutrition</a></li>
                <li><a href="#bmi">BMI Calculator</a></li>
                <li><a href="#tips">Tips for Beginners</a></li>
            </ul>
        </nav>
    </header>
    <section id="exercises" class="interactive">
        <h2>Exercises</h2>
        <!-- Exercise content here -->
    </section>
    <section id="nutrition" class="interactive">
        <h2>Nutrition and Diet Plans</h2>
        <!-- Nutrition content here -->
    </section>
    <section id="bmi" class="interactive">
        <h2>BMI Calculator</h2>
        <form method="post" action="/bmi">
            <label for="weight">Weight (kg):</label>
            <input type="number" id="weight" name="weight" required>

            <label for="height">Height (cm):</label>
            <input type="number" id="height" name="height" required>

            <button type="submit">Calculate</button>
        </form>
        {% if bmi_result %}
        <p id="bmi-result">Your BMI is {{ bmi_result }} ({{ bmi_category }}).</p>
        {% endif %}
    </section>
    <section id="tips" class="interactive">
        <h2>Tips for Beginners</h2>
        <!-- Tips content here -->
    </section>
    <footer>
        <p>&copy; 2024 Fitness Hub. All rights reserved.</p>
    </footer>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi_result = None
    bmi_category = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height']) / 100
            bmi = weight / (height * height)
            bmi_result = f"{bmi:.2f}"
            if bmi < 18.5:
                bmi_category = 'Underweight'
            elif bmi < 24.9:
                bmi_category = 'Normal weight'
            elif bmi < 29.9:
                bmi_category = 'Overweight'
            else:
                bmi_category = 'Obesity'
        except (ValueError, KeyError):
            bmi_result = "Invalid input"
    return render_template_string(html_template, bmi_result=bmi_result, bmi_category=bmi_category)

if __name__ == '__main__':
    app.run(debug=True)
