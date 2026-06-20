def filter_and_sort(data, key, value):
    filtered = [item for item in data if item.get(key) == value]
    sorted_data = sorted(filtered, key=lambda x: x['age'])
    return sorted_data

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35},
        {'name': 'Alice', 'age': 40}
    ]
    result = filter_and_sort(sample_data, 'name', 'Alice')
    print(result)