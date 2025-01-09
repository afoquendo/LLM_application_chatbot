from flask import Flask, request, render_template
from flask_cors import CORS		# newly added
import json

from ChatBot import chatbot

app = Flask(__name__)
CORS(app)

conversation_history = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']

    response = chatbot.get_response(input_text, conversation_history)

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    return response

if __name__ == '__main__':
    app.run()