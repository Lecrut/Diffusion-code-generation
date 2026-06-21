def group_by_keys(data, *keys):
    result = {}
    for item in data:
        keys_tuple = tuple(item[key] for key in keys)
        if keys_tuple not in result:
            result[keys_tuple] = []
        result[keys_tuple].append(item)
    return result

if __name__ == '__main__':
    sample_data = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 1, 'b': 3, 'c': 5},
        {'a': 2, 'b': 2, 'c': 6}
    ]
    grouped_data = group_by_keys(sample_data, 'a', 'b')
    print(grouped_data)