from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation.translator import english_to_french


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = english_to_french(textToTranslate)
    # Write your code here
    # return "Translated text to French"
    return translatedText
@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = french_to_english(textToTranslate)
    # return "Translated text to English"
    return translatedText

@app.route("/")
def renderIndexPage():
    render_template('index.html')
    # Write the code to render template


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
