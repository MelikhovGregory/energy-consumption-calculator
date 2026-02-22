import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_table(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE customers (
                            name TEXT,
                            email TEXT,
                            address TEXT,
                            date TEXT
                         )''')
        print('База данных была создана успешно.')

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()

    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
        
    
    def data_insert(self, name, email, address, date):
        sql = 'INSERT INTO customers VALUES(?, ?, ?, ?)'
        self.__executemany(sql, [(name, email, address, date)])


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_table()
