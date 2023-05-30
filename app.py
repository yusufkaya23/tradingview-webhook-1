from flask import Flask, request
import json
import telebot
from binance.spot import Spot as Client



app = Flask(__name__)




@app.route("/webhook", methods=['POST'])
def webhook():

    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        exchange = data['exchange']
        price = data['price']
        side = data['side']
        quantity = data['quantity']
        telegramBotApi = data['telegramBotApi']
        chatId = data['chatId']
        binanceApiKey = data['binanceApiKey']
        binanceSecretKey = data['binanceSecretKey']
        params = {
            "symbol": ticker,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
        }
        Client(binanceApiKey, binanceSecretKey).new_order(**params)
        telebot.TeleBot(telegramBotApi).send_message(chatId,
                                                     f"{ticker} \n{side} Emri geldi... \nFiyat : {price}  \nAlinanMiktar : {quantity} \nBEREKETLI KAZANÇLAR ")
    except:
        pass
    return {
        "code": "success",



    }










