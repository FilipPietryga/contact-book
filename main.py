import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database connection succeded!")
    except Error as err:
        print(f"Error: {err}")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Successful query!")
    except Error as err:
        print(f"Error: {err}")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: {err}")

def construct_insert_query(table, name, address, phone_number, email):
    return f"""
    INSERT INTO {table} VALUES
    ("{name}", "{address}", "{phone_number}", "{email}");
    """ 

print("Welcome to the contact_book program!")
while True:

    print("What do you want to do?")
    print("1. Show existing contacts")
    print("2. Add a contact")
    print("3. Exit")
    i = int(input())

    if(i == 1):
        connection = create_server_connection("localhost", "root", "Filip", "biblioteka")
        select_all = "SELECT * FROM contact_book;"
        results = read_query(connection, select_all)
        for result in results:
            print(result)
    elif(i == 2):
        print("insert data: ")
        name = input("name: ")
        address = input("address: ")
        phone_number = input("phone number: ")
        email = input("email: ")
        connection = create_server_connection("localhost", "root", "Filip", "biblioteka")
        insert_query = construct_insert_query("contact_book", name, address, phone_number, email)
        execute_query(connection, insert_query)
        print("Succesfully added new contact to the database!")
    elif(i == 3):
        exit()