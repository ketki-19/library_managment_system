import mysql.connector as ms

try:
    con = ms.connect(
        host="localhost",
        user="root",
        database="lbms",  # name your database here
        passwd="1502"  # enter your mysql passwd here
    )
    if con.is_connected():
        print("database connected")
    else:
        print("connection unsuccessful")
except Exception as e:
    print(f"MySQL Connection Error: {e}")
    print("Running in demo mode - MySQL features will be disabled")
    con = None
