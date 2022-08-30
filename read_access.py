#Goal - code to read accdb files
#Maria Kuruvilla
#15th Dec 2021

import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\maria\OneDrive\Documents\data\pied_piper\2020_Dungeness.accdb;')
# cursor = conn.cursor()
# cursor.execute('select * from table_name')
   
# for row in cursor.fetchall():
#     print (row)