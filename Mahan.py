from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# تابعی برای پاسخ به پیام‌ها
async def greet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    if message == "سلام":
        await update.message.reply_text("سلام! خوش اومدی")

# شروع ربات
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من یه ربات ساده‌ام.")

# توکن رباتت رو اینجا بذار
TOKEN = "7203768758:AAGLd6W4k68fIh0NY1DlPdGEH7eQq55Wuj0"

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), greet))

    print("ربات روشن شد...")
    app.run_polling()
