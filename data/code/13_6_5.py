def get_column_value(data, column_name):
    result = []
    for item in data:
        result.append(item[column_name])
    return result

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'San Francisco'},
        {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
    ]
    column_to_fetch = 'age'
    print(get_column_value(sample_data, column_to_fetch))