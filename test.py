import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Saroj@2000"
                        )
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE FSDS_DB")
#mycursor.execute("Use FSDS_DB")
mycursor.execute("USE sample_superstore")

# mycursor.execute("Create table Batch_db ( name varchar(50), syllabus varchar(50), batch int )")
#ycursor.execute("Insert into Batch_db values ('FSDS 2.0', 'Python', 1)")
mycursor.execute("select * from location")

for i in mycursor:
    print(i)

#mydb.commit()



