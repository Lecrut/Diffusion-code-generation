def get_column_value(data, column_name):
    return [item[column_name] for item in data]

if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
    result = get_column_value(sample_data, "name")
    print(result)