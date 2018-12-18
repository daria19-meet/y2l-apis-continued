from flask import Flask, render_template, request
import json, requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    headers = {'Authorization': 'Key f2f339a3cc374420a221fa27e58a3202'}

    image_url = request.form['url-input']
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
    
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    
    return render_template('home.html', results=json.loads(response.content))

if __name__ == '__main__':
    app.run(debug=True)