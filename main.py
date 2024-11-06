import telebot
from telebot import types
list_hi=['Привет']
# Объект бота
bot=telebot.TeleBot('8071247903:AAF0hawJrJpNLcqQ_zgbnnpXV0An1GI0efA')


@bot.message_handler(commands=['start'])
def send_hi(message):
    chat_id=message.chat.id
    keyboard=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton("🚀 Старт")
    button_support=telebot.types.KeyboardButton(text='🥰 Кнопка помощи')
    keyboard.add(start_button,button_support)
    bot.send_message(chat_id, 'У нас много интересного, спрашивайте!',reply_markup=keyboard)
#@bot.message_handler(commands=['start'])
#def start_message(message):
 #   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  #  start_button = types.KeyboardButton("🚀 Старт")
   # action_button = types.KeyboardButton("🥰 Комплимент")
    #markup.add(start_button, action_button)
    #bot.send_message(message.chat.id, text="Привет, {0.first_name} 👋\nВоспользуйся кнопками".format(message.from_user), reply_markup=markup)
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.from_user.id, 'Я тебя не понимаю.Напиши /help')



# Обработка сообщений при помощи функции декоратора
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in list_hi:
        bot.send_message(message.from_user.id,'Привет, чем я могу помочь?')
    elif message.text=='🥰 Кнопка помощи':
        bot.send_message(message.from_user.id, 'Как я могу помочь Вам?')
    elif message.text=='🚀 Старт':
        bot.send_message(message.from_user.id, 'Давайте выберем для Вас необходимую игрушку? Какой пол у вашего ребенка?')
    else:
        print(f'Пользователь{message.from_user.id} ну не так умён')
        bot.send_message(message.from_user.id,'Говорите по-русски')
# Запуск бота
bot.polling(none_stop=True, interval=0)
