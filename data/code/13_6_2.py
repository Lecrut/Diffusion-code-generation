def extract_column(data, column_name):
    results = []
    for record in data:
        if column_name in record:
            results.append(record[column_name])
    return results

if __name__ == '__main__':
    sample_data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    output = extract_column(sample_data, "name")
    print(output)