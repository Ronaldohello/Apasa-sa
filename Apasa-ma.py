import os

from flask import Flask, render_template_string, request

app = Flask(__name__)

# Inline HTML template (simpler than using separate files)
TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Ești prețios/prețioasă ♥</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #0f1724;
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .card {
      background: rgba(255, 255, 255, 0.05);
      padding: 30px;
      border-radius: 16px;
      text-align: center;
      width: 320px;
    }
    input {
      width: 100%%;
      padding: 10px;
      margin: 8px 0;
      border-radius: 8px;
      border: none;
    }
    button {
      background: #ff6b81;
      border: none;
      padding: 10px 16px;
      border-radius: 8px;
      color: white;
      font-weight: bold;
      cursor: pointer;
    }
    .heart {
      font-size: 60px;
      color: #ff4b6e;
      margin: 20px 0;
    }
  </style>
</head>
<body>
  <div class="card">
    {% if not name %}
      <h2>Spune-mi cum te numești?</h2>
      <form method="post">
        <input type="text" name="first" placeholder="Numele" required>
        <input type="text" name="last" placeholder="Nume de familie" required>
        <button type="submit">Trimite</button>
      </form>
    {% else %}
      <div class="heart">♥</div>
      <h2>Hey {{ name }}!</h2>
      <p>Ești special — Nu uita aceasta!</p>
      <a href="/">Înapoi</a>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first = request.form.get("first", "").strip()
        last = request.form.get("last", "").strip()
        full_name = f"{first} {last}".strip()
        return render_template_string(TEMPLATE, name=full_name)
    return render_template_string(TEMPLATE, name=None)


if __name__ == "__main__":
    # For local testing only. In production the host/port are handled by the host service (or gunicorn).
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
