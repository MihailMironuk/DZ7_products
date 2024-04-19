import sqlite3


def create_connection(hw_bd):
    conn = None
    try:
        conn = sqlite3.connect(hw_bd)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_products(connection, products):
    try:
        sql = '''INSERT INTO products
                 (product_title, price, quantity)
                 VALUES (?, ?, ?)
              '''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products(connection, products):
    try:
        sql = '''UPDATE products SET price = ?, quantity = ?
         WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def delete_products(connection, products_id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products_id)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_price(connection):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 and quantity > 5'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(e)


def select_products_by_name(connection, name):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + name + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(e)


sql_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INT NOT NULL DEFAULT 0
)
'''

my_connection = create_connection("hw.db")
if my_connection:
    print("Connected.")
    # create_table(my_connection, sql_products_table)
    # insert_products(my_connection, ('Бумага', 11, 21))
    # insert_products(my_connection, ('Часы', 110, 24))
    # insert_products(my_connection, ('Бульдозер', 1112, 2))
    # insert_products(my_connection, ('Дихлофос', 166, 12))
    # insert_products(my_connection, ('Перчатки', 72, 31))
    # insert_products(my_connection, ('Валидол', 17, 27))
    # insert_products(my_connection, ('Шоколадка Баунти', 121, 34))
    # insert_products(my_connection, ('Вареники с мясом', 155, 12))
    # insert_products(my_connection, ('Хозяйственное мыло', 44, 23))
    # insert_products(my_connection, ('Жидкий азот', 23, 241))
    # insert_products(my_connection, ('Стиральный порошок', 70, 14))
    # insert_products(my_connection, ('Полотенца бумажные', 20, 70))
    # insert_products(my_connection, ('Освежитель воздуха', 170, 41))
    # insert_products(my_connection, ('Губки', 36, 45))
    # insert_products(my_connection, ('Салфетки', 10, 213))

    # update_products(my_connection, (120, 10, 10))

    # delete_products(my_connection, [5])

    # select_all_products(my_connection)

    # select_products_by_price(my_connection)

    # select_products_by_name(my_connection, 'Бульдозер')

    my_connection.close()
