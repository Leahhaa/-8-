'''1. Открыть справочник
2. Сохраниить  справончик
3. Показть все контакты
4. Создать контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход'''
def open_book() ->None:
    book = open("number_book.txt", "r+", encoding='utf-8')
    book.write("hi")


def add_contact() -> None:
    with open("number_book.txt", "a+", encoding='utf-8') as book:
        book.seek(0)
        book.readlines()
        fio = input("Введите имя: ")
        number = input("Введите номер: ")
        comment = input("Введите комментарий: ")
        
        book.write(f"{fio},{number},{comment}\n")
        book.close

        

def all_contacts() -> list:
    with open("number_book.txt", "a+", encoding='utf-8') as book:
        return book.readlines()

def find_contacts() -> None:
    book = all_contacts()
    if (what := input("Что будете искать?\n(1 - ФИО, 2 - Номер, 3 - Комментарий): ")) == "1":
        fio = input("Введите имя: ")
        for contact in book:
            if fio in contact.lower():
                print(contact)
    elif what == "2":
        number = input("Введите номер: ")
        for contact in book:    
            if number in contact.lower():  
                print(contact)

    elif what == "3":
        comment = input("Введите комментарий: ")
        for contact in book:
            if comment in contact.lower():  
                print(contact)
    else:
        print("Неверный ввод. Пожалуйста, введите 1, 2 или 3.")

'''def change_contact() -> None:
    book = all_contacts()
    if (what := input("Что будете изменять?\n(1 - ФИО, 2 - Номер, 3 - Комментарий): ")) == "1":
        fio = input("Введите имя: ")
        changed_fio = input("Напишите измененное имя")
        for contact in book:
            if fio.lower in contact.lower(): не смог'''
# delete_contact()
# def delete_contact() -> str:
#     book = all_contacts()
#     if (what := input("кого будете удалять?\n(1 - удалить, 2 - выйти): ")) == "1":
#         fio = input("Введите имя: ")
#         book = [contact for contact in book if fio not in contact]
#         print("Контакт(ы) были удалены")
#     elif what == "2":
#         print("Вы вышли")

# delete_contact() почему то не работает

file = open("example.txt", "r")
file.close()