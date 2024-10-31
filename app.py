from flask import Flask, redirect, url_for, render_template,request,send_file
app = Flask(__name__)

@app.route('/')
def hello_world():
     return render_template('home.html')

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename)  

if __name__ == "__main__":
    app.run(debug=True)
    