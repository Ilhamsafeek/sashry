from flask import Flask, render_template, request,jsonify

from chat import get_response

app= Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route('/get_script_root')
def get_script_root():
    return jsonify(script_root=request.script_root)


if __name__ == "__main__":
    app.run(debug=True)