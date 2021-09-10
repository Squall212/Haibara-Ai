from telegram.ext import Updater, CommandHandler


def start(update, context):

    update.message.reply_text('Konbanwa, tantei-kun')

  


if __name__ == '__main__':

    updater = Updater(token='1780518008:AAHKl_RsLFwVXLpeGLYc9CtFe9u_vUz2Dxg', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    print('Iniciando Bot...')
    updater.idle()