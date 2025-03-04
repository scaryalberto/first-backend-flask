import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Ciao, il mio servizio Flask è su Railway!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Usa la porta fornita da Railway
    app.run(host='0.0.0.0', port=port)
