import sqlite3

def find_max_in_column(database_path, table_name, column_name):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    query = f"SELECT MAX({column_name}) FROM {table_name}"
    cursor.execute(query)
    
    max_value = cursor.fetchone()[0]
    
    cursor.close()
    conn.close()
    
    return max_value

if __name__ == '__main__':
    db_path = 'example.db'
    table = 'sample_table'
    column = 'sample_column'
    
    max_val = find_max_in_column(db_path, table, column)
    print(f"Table: {table}, Column: {column}, Max Value: {max_val}")