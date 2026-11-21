
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐉 M701 KNIFE SNIPER ishga tushdi!\n\n"
        "Steam Market pichoqlarini kuzatish tizimi tayyorlanmoqda.\n\n"
        "Buyruqlar:\n"
        "/start - Botni boshlash\n"
        "/status - Bot holati"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot ishlayapti!\n"
        "🔍 Steam Market kuzatuvi: hali ulanmagan."
    )

def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN topilmadi!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("M701 KNIFE SNIPER ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
