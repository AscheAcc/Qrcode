import telegram.ext, telegram
import pyqrcode
import sys 
API = TOKEN

def start(update, context):
        userId = update.message.chat_id
        userName = update.message.chat.first_name
        update.message.reply_text(f"Hi {userName} .")
def help(update, context):
    update.message.reply_text("c'est l'aide.. ")
def envoyer(update, context):
        url = update.message.text
        code = pyqrcode.create(url)
        code.png("YourQrCode.png", scale = 8)
        update.message.reply_text("This is your QR code: ")

        context.bot.sendPhoto(chat_id = update.message.chat_id, photo = open("YourQrCode.png", 'rb'), filename ="YourQrCode.png")
        update.message.reply_text("Thanks for using our bot \U0001F606 .")




                                                      
updater = telegram.ext.Updater(API, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, envoyer))

updater.start_polling()
updater.idle()

 
