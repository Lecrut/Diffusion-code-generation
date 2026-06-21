def group_items(data):
    grouped = {}
    for item in data:
        keys = tuple(item.get(key) for key in ['key1', 'key2', 'key3'])
        if keys not in grouped:
            grouped[keys] = []
        grouped[keys].append(item)
    return grouped

if __name__ == '__main__':
    sample_data = [
        {'key1': 'a', 'key2': 1, 'key3': 'x', 'value': 10},
        {'key1': 'b', 'key2': 2, 'key3': 'y', 'value': 20},
        {'key1': 'a', 'key2': 1, 'key3': 'x', 'value': 30},
        {'key1': 'c', 'key2': 3, 'key3': 'z', 'value': 40}
    ]
    print(group_items(sample_data))