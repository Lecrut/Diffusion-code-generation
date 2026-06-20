def filter_and_sort(data, key, value):
    return sorted([item for item in data if item.get(key) == value], key=lambda x: x['name'])

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Paris'},
        {'name': 'Charlie', 'age': 35, 'city': 'New York'},
        {'name': 'David', 'age': 40, 'city': 'London'}
    ]
    result = filter_and_sort(sample_data, 'city', 'New York')
    print(result)