import psycopg2

def create_db(conn):  
    with conn.cursor() as cur:                 
        cur.execute("""
        CREATE TABLE IF NOT EXISTS clients(
            client_id SERIAL PRIMARY KEY, 
            first_name VARCHAR(60) NOT NULL, 
            last_name VARCHAR(60) NOT NULL, 
            email VARCHAR(60) NOT NULL, 
            phones BIGINT,
            more_phones BIGINT 
        );
        """)
        conn.commit()

        cur.execute("""
        INSERT INTO clients(first_name, last_name, email, phones) VALUES
        ('Иван', 'Иванов', 'ivanov@mail.ru', 7915),
        ('Пётр', 'Петров', 'petrov@mail.ru', 7910),
        ('Николай', 'Сидоров', 'sidorov@mail.ru', 7919),
        ('Михаил', 'Попов', 'popov@mail.ru', 7999),
        ('Алексей', 'Петухов', 'petuhov@mail.ru', 7920);
         """)
        conn.commit()



def add_client(conn, first_name, last_name, email, phones=None):   
    new_data = [(first_name, last_name, email, phones)]
    with conn.cursor() as cur:
        for data in new_data:
            cur.execute("INSERT INTO clients(first_name, last_name, email, phones) VALUES (%s, %s, %s, %s)", data) 
        conn.commit()

def find_clients(conn):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM clients;
        """)
        print('Клиенты:', cur.fetchall())

def add_phone(conn, client_id, more_phones):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE clients SET more_phones=%s WHERE client_id=%s;
        """, (more_phones, client_id))
        conn.commit()

def change_client(conn, client_id, first_name, last_name, email, phones):
    with conn.cursor() as cur:
        if first_name == first_name:
            cur.execute("""
            UPDATE clients SET first_name=%s WHERE client_id=%s;
            """, (first_name, client_id))
            conn.commit()
        elif last_name == last_name:
            cur.execute("""
            UPDATE clients SET last_name=%s WHERE client_id=%s;
            """, (last_name, client_id))
            conn.commit()
        elif email == email:
            cur.execute("""
            UPDATE clients SET email=%s WHERE client_id=%s;
            """, (email, client_id))
            conn.commit()
        elif phones == phones:
            cur.execute("""
            UPDATE clients SET phones=%s WHERE client_id=%s;
            """, (phones, client_id))
            conn.commit()

def delete_phone(conn, client_id, phones):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE clients SET phones=%s WHERE client_id=%s;
        """, (phones, client_id))
        conn.commit()

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM clients WHERE client_id=%s;
        """, (client_id,))
        conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT first_name, last_name, email, phones FROM clients
        WHERE first_name = %s or last_name = %s or email = %s or phones = %s;
        """, (first_name, last_name, email, phones,))
        print(cur.fetchone())

print('Команды:\nc – создать базу данных;\na – добавить нового клиента;\nt – добавить телефон для клиента;\nu – изменить данные о клиенте;\ndt – удалить телефон клиента;\ndc – удалить клиента;\np – найти клиента;\npa – все клиенты;\nq - выход;')
with psycopg2.connect(database="clients", user="postgres", password="postgres") as conn:      
    def main():
        while True:
            user = input('Введите команду: ').lower()
            if user == 'c':
                create_db(conn)
                print('База данных успешно создана.')
            elif user == 'a':
                first_name = input('Введите имя: ')
                last_name = input('Введите фамилию: ')
                email = input('Введите почту: ')
                phones = input('Введите телефон: ')
                add_client(conn, first_name, last_name, email, phones=None)
                print('Новый клиент успешно добавлен.')
            elif user == 't':  
                client_id = input('Введите id клиента: ')
                more_phones = input('Введите телефон: ')
                add_phone(conn, client_id, more_phones)
                print('Данные успешно добавлены.')
            elif user == 'u':
                client_id = input('Введите id клиента: ')
                first_name = input('Введите имя: ')
                last_name = input('Введите фамилию: ')
                email = input('Введите почту: ')
                phones = input('Введите телефон: ')
                change_client(conn, client_id, first_name, last_name, email, phones)
                print('Данные успешно изменены.')
            elif user == 'dt':
                client_id = input('Введите id клиента: ')
                phones = None
                delete_phone(conn, client_id, phones)
                print('Телефон успешно удален.')
            elif user == 'dc':
                client_id = input('Введите id клиента: ')
                delete_client(conn, client_id)
                print('Клиент успешно удален.')
            elif user == 'p':
                first_name = input('Введите имя: ')
                last_name = input('Введите фамилию: ')
                email = input('Введите почту: ')
                phones = input('Введите телефон: ')
                find_client(conn, first_name, last_name, email, phones)
            elif user == 'pa':
                find_clients(conn)
            elif user == 'q':
                break
            else:
                print('Данная команда неверна')
    main()
conn.close()
   

    










