import mysql.connector
import pandas as pd
from proto import FLOAT


mydb = mysql.connector.connect(host="hostname",user="username",password="",database="SALES")


mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE ORDERS(ROWID INTEGER PRIMARY KEY, ORDERID VARCHAR(255), ORDERDATE VARCHAR(255), SHIPDATE VARCHAR(255), SHIPMODE VARCHAR(255), CUSTOMERID VARCHAR(255), CUSTOMERNAME VARCHAR(255), SEGMENT VARCHAR(255), COUNTRY VARCHAR(255), CITY VARCHAR(255), STATE VARCHAR(255), POSTALCODE INTEGER, REGION VARCHAR(255),POSTALID VARCHAR(255), CATEGORY VARCHAR(255), SUBCATEGORY VARCHAR(255), PRODUCTNAME VARCHAR(255), PRICE FLOAT)")