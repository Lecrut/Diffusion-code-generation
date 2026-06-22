import sqlite3

def validate_table_name(table_name):
    if not table_name:
        raise ValueError("Table name cannot be empty")

def get_column_names(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    return [column[1] for column in cursor.fetchall()]

def fetch_data_from_database(database_path, table_name):
    validate_table_name(table_name)
    
    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()
        columns = get_column_names(cursor, table_name)
        
        query = f"SELECT {', '.join(columns)} FROM {table_name}"
        cursor.execute(query)
        data = cursor.fetchall()
        
        return columns, data

def find_max_for_columns(data):
    max_values = {}
    for row in data:
        for column, value in zip(data[0], row):
            if column not in max_values or value > max_values[column]:
                max_values[column] = value
    return max_values

if __name__ == '__main__':
    database_path = 'example.db'
    table_name = 'sample_table'
    
    columns, data = fetch_data_from_database(database_path, table_name)
    max_values = find_max_for_columns(data)
    
    print("Maximum values for each column:")
    for column, value in max_values.items():
        print(f"{column}: {value}")