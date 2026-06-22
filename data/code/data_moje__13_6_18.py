def get_column_value(data, column_name):
    if not data:
        return []
    results = []
    for item in data:
        if column_name in item:
            results.append(item[column_name])
        else:
            results.append(None)
    return results

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 35}
    ]
    column_name = "name"
    values = get_column_value(sample_data, column_name)
    print(values)