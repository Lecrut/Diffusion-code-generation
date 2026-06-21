from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        if key in item:
            category = item[key]
            grouped[category].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'city': 'New York'},
        {'name': 'Bob', 'city': 'Los Angeles'},
        {'name': 'Charlie', 'city': 'New York'},
        {'name': 'David', 'city': 'Chicago'},
        {'name': 'Eve', 'city': 'Los Angeles'}
    ]
    grouped_data = group_by_key(sample_data, 'city')
    print(grouped_data)