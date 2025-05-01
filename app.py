from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Linux-Plus Demo</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Bootstrap 5 CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-color: #333333;
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
            }
            .hero {
                background: linear-gradient(135deg, #1793d1, #1abc9c);
                color: white;
                padding: 60px 20px;
                text-align: center;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }
            .footer {
                margin-top: 40px;
                padding: 10px;
                text-align: center;
                color: #8b949e;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>

        <div class="container mt-5">
            <div class="hero">
                <h1 class="display-4">Linux-Plus Technical Team</h1>
                <p class="lead">Hello from <strong>GitHub Actions</strong> and <strong>OpenShift</strong>!</p>
                <hr class="my-4">
                <p>This modern demo is powered by Flask & deployed with CI/CD 🚀</p>
            </div>

            <div class="footer">
                &copy; 2025 Linux-Plus | Built with ❤️ using Flask and adel
            </div>
        </div>

        <!-- Bootstrap 5 JS -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
