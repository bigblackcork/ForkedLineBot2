import os
from flask import Flask, request, abort, jsonify
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['4yC+Q+HuPAtIHmKSL6KjC6yA9tOiVQ5gFd8Bqhy00A+riGpkUNg/PbVwVvKs/7KABxJBQ3CmgWqB5+HsMEjSTWt6fjD4LWQ4vQtF5lLH1Ogn+5/75o7mARBRZEneMsOqDy+fNeH2+H8qzuA8O9dZXAdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['caadf9bd28b0c46e8b6a6558cbd31b86'])

@app.route("/")
def index():
    return "Hello World สวัสดีชาวโลก", 200

@app.route("/callback", methods=['POST'])
def callback():
#    return "ok"
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK', 200


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
#        TextSendMessage(text=event.message.text)
        TextSendMessage(text="สบายดีไหม")
    )


if __name__ == "__main__":
    app.run()
