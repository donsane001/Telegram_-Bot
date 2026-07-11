import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

IMAGE_URL = "https://badmickey.netlify.app/logo.png"  # Change this if you host your image elsewhere

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🛒 Buy",
                url="https://pump.fun/coin/4wd7faasQAakmYmNokeQ9aA1Czq27DYHEDChUYxppump"
            ),
            InlineKeyboardButton(
                "🚀 Pump.fun",
                url="https://pump.fun/coin/4wd7faasQAakmYmNokeQ9aA1Czq27DYHEDChUYxppump"
            ),
        ],
        [
            InlineKeyboardButton(
                "❌ X",
                url="https://x.com/BadMickeycoin"
            ),
            InlineKeyboardButton(
                "🌐 Website",
                url="https://badmickey.netlify.app/"
            ),
        ],
    ]

    text = (
        "🖤 <b>BADMICKEY</b>\n\n"
        "The darkest mouse on Solana has arrived.\n\n"
        "<b>CA</b>\n"
        "<code>4wd7faasQAakmYmNokeQ9aA1Czq27DYHEDChUYxppump</code>"
    )

    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
