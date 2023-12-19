import sqlite3
import csv
from person import Person
import os

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')

    def createTable(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE if not exists people
                (first_name TEXT, last_name TEXT, address TEXT)''')
        
    def insert(self, person: Person):
        c = self.conn.cursor()
        query = f"""INSERT INTO people(first_name, last_name, address)
            VALUES('{person.first_name}', '{person.last_name}', '{person.address}')"""
        c.execute(query)
        
    def saveAndCommit(self):
        self.conn.commit()

data =[
     ['imie', 'nazwisko', 'adres'],
['Sylwia', 'Szetela', 'Jeziorna 17'],
['Weronika', 'Grzeszczuk', 'Centralna 54'],
['Tymoteusz', 'Popiński', 'Kirasjerów 130'],
['Marcelina', 'Marko', 'Jodłowa 90'],
['Przemysław', 'Opolski', 'Puławskiego 108']
]

file_path = 'data.csv'



if __name__ == "__main__":
    file_path = os.path.abspath('data.csv')

class CsvReader:
    def ReadCsv(file_path):
        persons = []

        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                person = Person(row[0], row[1], row[2])
                persons.append(person)

        return persons

all_people = CsvReader.ReadCsv(file_path)

person_db = Database()
person_db.createTable()

for p in all_people:
    person_db.insert(p)

try:
    person_db.saveAndCommit()
except sqlite3.Error as e:
    print("Error inserting data:", e)

with open(file_path, 'w', newline="") as file_csv:
    writer = csv.writer(file_csv)
    for person in data:
        writer.writerow(person)
