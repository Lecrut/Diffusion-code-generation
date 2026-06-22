def get_column_values(data, column_name):
    return [item[column_name] for item in data]

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 30},
        {'id': 2, 'name': 'Bob', 'age': 25},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    column_to_fetch = 'name'
    result = get_column_values(sample_data, column_to_fetch)
    print(result)