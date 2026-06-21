def fetch_column_value(data, column_name):
    if not data:
        return None
    if column_name not in data[0]:
        raise KeyError(f"Column '{column_name}' not found in schema")
    return [item[column_name] for item in data]

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 35}
    ]
    result = fetch_column_value(sample_data, "name")
    print(result)