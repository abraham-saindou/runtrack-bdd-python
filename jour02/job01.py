import mysql.connector

connector = mysql.connector.connect(host='localhost', database='LaPlateforme', user='abraham', password='abraham')
if connector.is_connected():
    db_info = connector.get_server_info()
    print(f"Connected to MySql server version {db_info}")
    cursor = connector.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database ", record)
    table_etudiants = "select * from etudiants;"
    cursor.execute(table_etudiants)
    data = cursor.fetchone()