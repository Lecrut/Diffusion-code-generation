def get_column_values(data, column_name):
    if not data:
        return []
    if column_name not in data[0]:
        raise KeyError(f"Column '{column_name}' not found in data")
    return [row[column_name] for row in data]

if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "score": 95},
        {"id": 2, "name": "Bob", "score": 88},
        {"id": 3, "name": "Charlie", "score": 92}
    ]
    result = get_column_values(sample_data, "name")
    print(result)