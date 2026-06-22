def get_column_values(data, column_name):
    result = []
    for record in data:
        if column_name in record:
            result.append(record[column_name])
    return result

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 35}
    ]
    column_name = "name"
    values = get_column_values(sample_data, column_name)
    print(values)