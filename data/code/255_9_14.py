import sqlite3

def find_max_values():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('\n        CREATE TABLE sample (\n            id INTEGER PRIMARY KEY,\n            col1 INTEGER,\n            col2 INTEGER,\n            col3 INTEGER\n        )\n    ')
    cursor.executemany('INSERT INTO sample (col1, col2, col3) VALUES (?, ?, ?)', [(10, 20, 30), (40, 50, 60), (70, 80, 90)])
    cursor.execute('SELECT MAX(col1), MAX(col2), MAX(col3) FROM sample')
    max_values = cursor.fetchone()
    return max_values
if __name__ == '__main__':
    max_values = find_max_values()
    print(f'Max values: col1={max_values[0]}, col2={max_values[1]}, col3={max_values[2]}')