import mysql.connector

try:
    connction = mysql.connector.connect(host = 'localhost', user = 'root', password = 'EchoMySQL2024')

    cursor = connction.cursor()
    create_db = "CREATE DATABASE IF NOT EXISTS alx_book_store;"
    cursor.execute(create_db)
        

except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")

finally:
    if connction.is_connected():
        print("Database 'alx_book_store' created successfully!")
        cursor.close()
        connction.close()
    else:
        print("Connection is not established")
