def fetch_column_value(data_list, column_name):
    if not data_list:
        return []
    result = []
    for item in data_list:
        if column_name in item:
            result.append(item[column_name])
    return result

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 88},
        {"id": 3, "name": "Charlie", "score": 92}
    ]
    target_column = "name"
    retrieved_values = fetch_column_value(sample_data, target_column)
    print(retrieved_values)