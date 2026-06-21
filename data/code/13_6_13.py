def fetch_column_values(data, column_name):
    return [row[column_name] for row in data]

if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
    column = "name"
    result = fetch_column_values(sample_data, column)
    print(result)