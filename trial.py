from flask import Flask
from flask import request
from flask import jsonify
#code which helps initialize our server
app = Flask(__name__)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
@app.route('/', methods=['POST'])
def result():
   print("enered")
   img=request.data
   print(img)
   phone=["02236212522"]
   name=["nourhan","mohamed"]
   return jsonify(names=name,phones=phone)

@app.route('/ur', methods=['GET'])
def res():
   print ("Here")
   return("Hello")
    
