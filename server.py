""" Main server file
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_analyzer():
    """ Returns text of emotion analyzer output
    """
    text_to_analyze = request.args.get('textToAnalyze')
    obj = emotion_detector(text_to_analyze)
    if obj['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return {"For the given statement ,the system respose is": obj,
    "The dominant emotion is": obj['dominant_emotion']}

@app.route("/")
def render_index_page():
    """ Render index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
   