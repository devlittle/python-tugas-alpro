import pymysql.cursors

# Open database connection
db = pymysql.connect("localhost","root","hackmeid","hackmeid" )
cursor = db.cursor()


cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
db.close()

#Membuat Tabel Database
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)
db.close()

#Operasi Insert
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()


#Read Operation
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      print ("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")
db.close()


#Update Operation
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()


#Delete Operation
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
db.close()