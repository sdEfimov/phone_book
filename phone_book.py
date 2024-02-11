# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
#    (Например имя или фамилию человека)
# main.py
FILE_NAME = 'phone_book.txt'
DATA_INPUT = ['введите фамилию: ', 'введите имя: ', 'введите отчество: ',
               'введите номер телефона: ', 'введите комментарий: ']
DATA_SEARCH = ['поиск по фамилии: ', 'поиск по имени: ', 'поиск по отчеству: ',
                'поиск по номер телефона: ', 'поиск по комментарию: ']
DATA_REPLACE = ['заменить фамилию: ', 'заменить имя: ', 'заменить отчество: ',
               'заменить номер телефона: ', 'заменить комментарий: ']

from typing import List

def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    if len(data) == 0:
        print("Данные в файле отсутствуют")
    for line in data:
        print(line)
    
def save_data(file):
    print('Введите данные контакта:')
    last_name = input(DATA_INPUT[0])
    first_name = input(DATA_INPUT[1])    
    patronymic = input(DATA_INPUT[2])
    phone_number = input(DATA_INPUT[3])
    comment = input(DATA_INPUT[4])
    print()
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}, {comment}\n')

def data_menu(DATA_: List[str]):
    type_is = True
    while type_is:
        print('0 - назад')
        print('1 - ', DATA_[0])
        print('2 - ', DATA_[1])
        print('3 - ', DATA_[2])
        print('4 - ', DATA_[3])
        print('5 - ', DATA_[4])
        try:
            answer = int(input('Выберите действие: '))
            type_is = False
        except ValueError:
            print("необходимо ввести число")
        print()
    return answer

def search_data(contacts: List[str]):
    # ['Иван, Иванов, Иванович, 123', 'Петр, Иванов, Петрович, 456']
    answer = data_menu(DATA_SEARCH)
    founded = []
    if answer == 0:
        return founded
    search_str = input(DATA_INPUT[answer-1])
    
    # search_idx
    index = 1
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[answer-1].lower():
            contact = str(index) + ", " + contact
            founded.append(contact)
            index = index + 1
    return founded

def answers(answer):
    if answer == '0':
        return False
    
    elif answer == '1':
        save_data(FILE_NAME)

    elif answer == '2':
        data = read_file(FILE_NAME)
        show_data(data)

    elif (answer == '3') or (answer == '4') or (answer == '5'):
        data = read_file(FILE_NAME)
        founded_data = search_data(data)
        if len(founded_data)==0:
            print("данные не были найдены")
            print()
        else:
            show_data(founded_data)
#----------------------------------------------------------------------------------------
        if (answer == '4') or (answer == '5'):
            str_number = 1
            if len(founded_data) > 1:
                print("Было найдено более одной записи")
                str_number = input("Введите номер записи: ")
                print()
            new_line = founded_data[int(str_number)-1].replace(str_number + ", ", "")
            with open(FILE_NAME, 'w', encoding='utf-8') as f:
                f.write("")
#----------------------------------------------------------------------------------------
            if answer == '4':
                answer = data_menu(DATA_REPLACE)           
                replace_str = input(DATA_INPUT[answer-1])
                    #new_line_list = []
                    # new_line_list = new_line.split(", ")
                    # new_line_list[answer-1] = replace_str
                    # new_line = ", ".join(new_line_list)
                for line in data:
                    if new_line == line:
                        new_line_list = new_line.split(", ")
                        new_line_list[answer-1] = replace_str
                        line = ", ".join(new_line_list)
                        if answer == 5:
                            line = line + "\n"
                    with open(FILE_NAME, 'a', encoding='utf-8') as f:
                        f.write(line)
                print("данные были заменены")       
#----------------------------------------------------------------------------------------
            elif answer == '5':                     
                for line in data:
                    if new_line != line:
                        with open(FILE_NAME, 'a', encoding='utf-8') as f:
                            f.write(line)
                print("данные были удалены") 

    return True
    

def main():
    #file_name = 'phone_book.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - редактировать запись')
        print('5 - удалить запись')
        answer = input('Выберите действие: ')
        print()
        flag=answers(answer)       

if __name__ == '__main__':
    main()
