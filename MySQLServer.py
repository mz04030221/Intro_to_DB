"""
import mysql.connector
mysql.connector.connect
except mysql.connector.Error
"""

import mariadb

connection = mariadb.connect(user="root", password="12500", host="localhost")

cursor = connection.cursor()

try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
except Exception as e:
    print(e)
else:
    print("Database 'alx_book_store' created successfully!")

connection.close()
