def get_column_values(data, column_name):
    values = []
    for row in data:
        if column_name in row:
            values.append(row[column_name])
    return values

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 35}
    ]
    result = get_column_values(sample_data, "name")
    print(result)