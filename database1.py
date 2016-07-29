import mysql.connector
from mysql.connector import Error


def connect():
    try:
        conn = mysql.connector.connect(host='localhost', database='login',
                                       user='root', password='suman')
        if conn.is_connected():
            print("Database connection successfull !")
    except Error as e:
        print(e)

    finally:
        conn.close()

