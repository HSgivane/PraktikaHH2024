#Telegram
TOKEN = ''

start_msg = '''
Вас приветствует помощник для нахождения вакансий на платформе hh.ru.
Мой автор: Живодров Иван, группа – БВТ2205.
'''

def vacancy_msg(vacancy_name, company, salary, city, url):
    msg = f'Вакансия: {vacancy_name}\nКомпания: {company}\nЗарплата: {salary}\nГород: {city}\nСсылка: {url}'
    return msg
    
help = '''
Запустить бота /start
Посмотреть вакансии /vacancy
Список комманд /help
'''