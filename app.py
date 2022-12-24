from flask import Flask, request, abort
from json import loads
import requests

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
    try:
        payload = loads(request.data)
        # Payload docs: https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads
        message = "%s\nLink: %s" % (payload["head_commit"]["message"], payload["head_commit"]["url"])
        r = requests.get("https://api.telegram.org/bot{"bot token"}/sendMessage?chat_id={"chat_id"}&text=message)
    except:
        abort(400)

    return "Ok!"

if __name__ == "__main__":
    # This code is new     app.debug = True
    # --&gt;
    app.run(host="0.0.0.0", port=4567)