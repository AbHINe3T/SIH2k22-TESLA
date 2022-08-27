import mysql.connector

mydb = mysql.connector.connect(
       host= "databasesih.cdj6dkht0ydp.us-east-1.rds.amazonaws.com",
       user="admin",
       password="admin123",
       database="Attendance_sih1"

)
a = mydb.cursor()
#a.execute("CREATE DATABASE Attendance_sih1")
a.execute("CREATE TABLE UserAttendance (Date VARCHAR(30),USERNAME VARCHAR(255),DateTime VARCHAR(255),roll VARCHAR(255), PRIMARY KEY (Date,USERNAME,roll))")
#a.execute("use attendance")
mydb.commit()
mydb.close()
