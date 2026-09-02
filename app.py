from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "🤖 Bot de Facebook funcionando correctamente."

@app.route("/webhook")
def webhook():
    return "Webhook preparado."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

