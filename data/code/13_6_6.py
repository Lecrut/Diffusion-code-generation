def fetch_column_value(data, column_name):
    return [record[column_name] for record in data]

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 88},
        {"id": 3, "name": "Charlie", "score": 92}
    ]
    target_column = "name"
    result = fetch_column_value(sample_data, target_column)
    print(result)