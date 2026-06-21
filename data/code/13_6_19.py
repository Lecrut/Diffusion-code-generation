def get_column_values(data, column_name):
    return [row[column_name] for row in data]

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'San Francisco'},
        {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
    ]
    result = get_column_values(sample_data, 'name')
    print(result)