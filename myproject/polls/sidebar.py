from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Nhome')
def home():
    return render_template('index.html')

@app.route('/Admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/AddEbike')
def add_ebike():
    return render_template('add_ebike.html')

@app.route('/AddAssignment')
def add_assignment():
    return render_template('add_assignment.html')

@app.route('/AddParts')
def add_parts():
    return render_template('add_parts.html')

@app.route('/Sales')
def sales():
    return render_template('sales.html')

if __name__ == '__main__':
    app.run(debug=True)
