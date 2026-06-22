import sqlite3

def find_max_values():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('\n        CREATE TABLE sample_table (\n            id INTEGER PRIMARY KEY,\n            col1 INTEGER,\n            col2 REAL,\n            col3 TEXT\n        )\n    ')
    cursor.executemany('INSERT INTO sample_table (col1, col2) VALUES (?, ?)', [(10, 1.5), (20, 2.5), (30, 3.5)])
    cursor.execute('SELECT MAX(col1), MAX(col2) FROM sample_table')
    max_values = cursor.fetchone()
    return max_values
if __name__ == '__main__':
    max_col1, max_col2 = find_max_values()
    print(f'Maximum value in col1: {max_col1}')
    print(f'Maximum value in col2: {max_col2:.1f}')