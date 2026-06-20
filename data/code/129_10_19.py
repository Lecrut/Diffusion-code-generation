def filter_and_sort(data, key, value):
    filtered = [item for item in data if item.get(key) == value]
    sorted_data = sorted(filtered, key=lambda x: x['score'], reverse=True)
    return sorted_data

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 92},
        {'name': 'Charlie', 'score': 78},
        {'name': 'David', 'score': 92},
        {'name': 'Elderberry', 'score': 88}
    ]
    result = filter_and_sort(sample_data, 'name', 'Bob')
    print(result)