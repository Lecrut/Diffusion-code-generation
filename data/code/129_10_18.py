def filter_and_sort(data, key, value, sort_key):
    filtered = [item for item in data if item.get(key) == value]
    sorted_data = sorted(filtered, key=lambda x: x[sort_key])
    return sorted_data

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'name': 'Bob', 'age': 30, 'city': 'Chicago'},
        {'name': 'Charlie', 'age': 35, 'city': 'San Francisco'},
        {'name': 'David', 'age': 40, 'city': 'New York'}
    ]
    result = filter_and_sort(sample_data, 'city', 'New York', 'age')
    print(result)