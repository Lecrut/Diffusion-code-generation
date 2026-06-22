import sqlite3

class DatabaseMaxFinder:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def find_max_values(self, table_name):
        query = f"SELECT max({column}) FROM {table_name} FOR EACH COLUMN"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return {column: value for column, value in zip(self.cursor.description, [row[0] for row in results])}

    def close_connection(self):
        self.connection.close()

if __name__ == '__main__':
    db_path = 'sample.db'
    table_name = 'numbers_table'
    
    finder = DatabaseMaxFinder(db_path)
    max_values = finder.find_max_values(table_name)
    finder.close_connection()
    
    for column, value in max_values.items():
        print(f"Column: {column}, Max Value: {value}")