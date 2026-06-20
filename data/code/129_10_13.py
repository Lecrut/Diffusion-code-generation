def filter_and_sort(data, key, value):
    filtered = [item for item in data if item.get(key) == value]
    sorted_data = sorted(filtered, key=lambda x: x['age'], reverse=True)
    return sorted_data

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35},
        {'name': 'David', 'age': 25}
    ]
    result = filter_and_sort(sample_data, 'age', 25)
    print(result)