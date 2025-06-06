import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from binance.client import Client

# API võtmed
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

# Binance client
client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_SECRET_KEY)

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = client.futures_symbol_ticker(symbol="BTCUSDT")['price']
    await context.bot.send_message(chat_id=CHANNEL_ID, text=f"📈 BTCUSDT: {price}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("signal", signal))
    app.run_polling()
