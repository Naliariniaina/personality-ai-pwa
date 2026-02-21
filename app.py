from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_personality(scores):
    result = {}

    if scores["openness"] >= 3:
        result["Openness"] = "Creative and curious."
    else:
        result["Openness"] = "Practical and realistic."

    if scores["conscientiousness"] >= 3:
        result["Conscientiousness"] = "Organized and disciplined."
    else:
        result["Conscientiousness"] = "Flexible and spontaneous."

    if scores["extraversion"] >= 3:
        result["Extraversion"] = "Outgoing and energetic."
    else:
        result["Extraversion"] = "Reserved and thoughtful."

    if scores["agreeableness"] >= 3:
        result["Agreeableness"] = "Kind and cooperative."
    else:
        result["Agreeableness"] = "Independent and competitive."

    if scores["neuroticism"] >= 3:
        result["Neuroticism"] = "Emotionally sensitive."
    else:
        result["Neuroticism"] = "Calm and stable."

    return result


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        scores = {
            "openness": int(request.form["q1"]),
            "conscientiousness": int(request.form["q2"]),
            "extraversion": int(request.form["q3"]),
            "agreeableness": int(request.form["q4"]),
            "neuroticism": int(request.form["q5"]),
        }

        result = analyze_personality(scores)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)