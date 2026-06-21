def fetch_column_value(data, column_name):
    result = []
    for record in data:
        if column_name in record:
            result.append(record[column_name])
    return result

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 88},
        {"id": 3, "name": "Charlie", "score": 92}
    ]
    column_name = "name"
    values = fetch_column_value(sample_data, column_name)
    print(values)