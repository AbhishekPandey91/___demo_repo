from flask import Flask, request, render_template_string, redirect
import sqlite3
import os
import pickle
import subprocess
app = Flask(__name__)
DATABASE_USER = "admin"
DATABASE_PASSWORD = os.getenv("SECRET_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
API_KEY = os.getenv("SECRET_KEY")
# TODO: Fix csrf
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = fos.getenv("SECRET_KEY"){username}os.getenv("SECRET_KEY"){password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        return "Login successful!"
    return "Login failed!"
@app.route('/ping')
def ping():
    host = request.args.get('host', 'localhost')
    result = os.system(f"ping -c 4 {host}")
    return f"Ping result: {result}"
@app.route('/read_file')
def read_file():
    filename = request.args.get('file')
    with open(filename, 'r') as f:
        content = f.read()
    return content
@app.route('/search')
def search():
    query = request.args.get('q', '')
    template = f"""
    <html>
        <body>
            <h1>Search Results for: {query}</h1>
            <p>Your search: {query}</p>
        </body>
    </html>
    """
    return render_template_string(template)
# TODO: Fix csrf
@app.route('/load_data', methods=['POST'])
def load_data():
    data = request.data
# TODO: Fix insecure_deserialization
    obj = pickle.loads(data)
    return f"Loaded: {obj}"
@app.route('/admin/delete_user/<user_id>')
def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id={user_id}")
    conn.commit()
    return f"User {user_id} deleted!"
# TODO: Fix csrf
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password'] 
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()
    return "User registered!"
# TODO: Fix csrf
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f"uploads/{file.filename}")
    return "File uploaded!"
@app.route('/debug')
def debug():
    return {
        'env_vars': dict(os.environ),
        'secret_key': SECRET_KEY,
        'database_password': DATABASE_PASSWORD
    }
@app.route('/fetch_url')
def fetch_url():
    import urllib.request
    url = request.args.get('url')
    response = urllib.request.urlopen(url)
    return response.read()
@app.route('/create_invoice')
def create_invoice():
    invoice_id = request.args.get('id')
    filename = f"invoice_{invoice_id}.txt"
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write("Invoice data")
    return "Invoice created"
if __name__ == '__main__':
# TODO: Fix debug_code
    app.run(debug=True, host='0.0.0.0', port=5000)

