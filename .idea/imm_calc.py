import datetime
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

from telegramcalendar import create_calendar, process_calendar_selection


current_time = datetime.datetime.now()
CALENDAR, STEP = range(2)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""Привет! Я помогу тебе разобраться в правилах,
     Введи дату своего въезда""")

async def count_arrivals(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [[InlineKeyboardButton("Выбрать дату", callback_data='calendar')]]
    reply_markup = InlineKeyboardMarkup(keyboard)


    message_text = f"Количество дней нахождения в Турции {delta_days}"

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message_text)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6282016707:AAF5_Es-umpoJ4hKnnk15KOayS0q3QIMoYY').build()


    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)


    application.run_polling()