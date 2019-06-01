import os
import datetime
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(host = 'localhost', user = username, password = '', db = 'Chinook')

try:
    
    ## Exercise 1 -- conecting with MySQL
    # with connection.cursor() as cursor:
    #     sql = input("Enter SQL Query: ")
    #     sql = "SELECT * FROM Artist LIMIT 50;"
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     print(result)
        
    ## Exercise 2 -- Using Cursor
    # with connection.cursor(pymysql.cursors.DictCursor) as cursor:
    #     sql = "SELECT * FROM Genre"
    #     cursor.execute(sql)
    #     for row in cursor:
    #         print(row)
        
    ## Exercise 3 -- Creating Table from Python
    # with connection.cursor() as cursor:
    #     cursor.execute("""CREATE TABLE IF NOT EXISTS
    #                       Friends(name char(20), age int, DOB datetime);""")
        
    ## Exercise 4 -- Inserting data
    # with connection.cursor() as cursor:
    #     row = ("Bob", 21, "1990-02-06 23:04:56")
    #     cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
    #     connection.commit()
        
    ## Exercise 5  -- inserting multiple rows
    # with connection.cursor() as cursor:
    #     rows = [("Bob", 21, "1990-02-06 23:04:56"),
    #             ("Jim", 56, "1955-05-09 13:12:45"),
    #             ("Fred", 100, "1911-09-12 01:01:01")]
    #     cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
    #     connection.commit()
    
    ## Exercise 6 -- Updating data 
    # with connection.cursor() as cursor:
    #     cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
    #     connection.commit()
        
    ## Exercise 7 -- Updating data using interpolation
    # with connection.cursor() as cursor:
    #     cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;", (23, 'Bob'))
    #     connection.commit()
    
    ## Exercise 8 -- Updating multiple rows
    # with connection.cursor() as cursor:
    #     rows = [(23, 'Bob'),
    #             (24, 'Jim'),
    #             (25, 'Fred')]
        
    #     cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
    #     connection.commit()
        
    ## Exercise 9 -- Deleting data
    # with connection.cursor() as cursor:
    #     rows = cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
    #     print("DELETED ROWS: {}".format(rows))
    #     connection.commit()
            
    ## Exercise 10 -- Deleting using string interpolation
    # with connection.cursor() as cursor:

    #     ## Insert 'bob' if deleted in the previous exercise
    #     # cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", ("Bob", 21, "1990-02-06 23:04:56"))
    #     # connection.commit()
        
    #     rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Bob')
    #     print("DELETED ROWS: {}".format(rows))
    #     connection.commit()
        
    ## Exercise 11 -- Deleting many rows
    # with connection.cursor() as cursor:

    #     ## Insert 'bob' if deleted in the previous exercise
    #     # cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", ("Bob", 21, "1990-02-06 23:04:56"))
    #     # connection.commit()
        
    #     rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob', 'Jim'])
    #     print("DELETED ROWS: {}".format(rows))
    #     connection.commit()
        
    ## Exercise 12 -- Deleting many rows using SQL "WHERE IN" query
    with connection.cursor() as cursor:

        ## Insert 'Bob' and 'Jim' if deleted in the previous exercise
        # cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", [("Bob", 21, "1990-02-06 23:04:56"), ("Jim", 56, "1955-05-09 13:12:45")])
        # connection.commit()
        
        ## Part 1 - hardcoded qurery
        # names = ['Bob', 'Jim']
        # cursor.execute("DELETE FROM Friends WHERE name in (%s, %s);", names)
        
        ## Part 2 - programaticly set query
        list_of_names = ['Bob', 'Jim']
        format_strings = ','.join(['%s'] * len(list_of_names))
        query = "DELETE FROM Friends WHERE name in ({});".format(format_strings)
        print(query)
        rows = cursor.execute( query, list_of_names)
            
        print("DELETED ROWS: {}".format(rows))
        connection.commit()
        
        ## This code confirms the changes were completed
        cursor.execute("SELECT * FROM Friends;")
        for line in cursor:
            print(line)
        
finally:
    connection.close()
    