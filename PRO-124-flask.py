from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [
    {
        "Contact" : 1234567890,
        "Name" : "David",
        "id" : 1,
        "done" : False
    },
    {
        "Contact" : 9876543210,
        "Name" : "Shawn",
        "id" : 2,
        "done" : False
    }
]    

@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
    else:
        contact = {
            "Contact" : request.json["Contact"],
            "Name" : request.json["Name"],
            "id" : contacts[-1]["id"] + 1,
            "done" : False
        }
        contacts.append(contact)
        return jsonify(
            {
            "Status" : "Success",
            "Message": "Contact added succesfully!"
        },
        {
            "data":contacts
        }
        )

if (__name__ == "__main__"):
    app.run(debug=True)