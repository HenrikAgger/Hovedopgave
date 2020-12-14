
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "hovedopgave"
)
    
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM descriptions")

table_rows = mycursor.fetchall()

#table_rows = db_cursor.fetchall()

#pandas.set_option('display.max_rows', df.shape[0]+1)
df = pd.DataFrame(table_rows)

print(df.head(None))

#for row in myresult:
#    print(row)

#data = pd.read_sql(myresult)
#print(data)


words_building_condition = ['håndværkertilbud', 'dårlig stand', 'nedrivning'] # dårlig elendig faldefærdig - stand

words_location = ['udsigt', 'grund'] # god fremragende fantastisk

# 1a) Led efter ord som siger noget om bygningens tilstand eller placering.
# 1b) Led efter ord som siger noget om bygningens (dårlige) tilstand eller (gode) placering.

# 2) Find de tekster som siger noget om tilstanden eller placeringen 

# 3)

