def group_by_keys(data, *keys):
    grouped = {}
    for item in data:
        key_tuple = tuple(item[key] for key in keys)
        if key_tuple not in grouped:
            grouped[key_tuple] = []
        grouped[key_tuple].append(item)
    return grouped

if __name__ == '__main__':
    sample_data = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 2, 'b': 3, 'c': 4},
        {'a': 1, 'b': 2, 'c': 3}
    ]
    print(group_by_keys(sample_data, 'a', 'b'))