def group_by_keys(data, *keys):
    result = {}
    for item in data:
        keys_tuple = tuple(item[key] for key in keys)
        current_level = result
        for key in keys_tuple[:-1]:
            if key not in current_level:
                current_level[key] = {}
            current_level = current_level[key]
        last_key = keys_tuple[-1]
        if last_key not in current_level:
            current_level[last_key] = []
        current_level[last_key].append(item)
    return result

if __name__ == '__main__':
    data = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 1, 'b': 2, 'c': 4},
        {'a': 1, 'b': 3, 'c': 5},
        {'a': 2, 'b': 2, 'c': 6}
    ]
    grouped_data = group_by_keys(data, 'a', 'b')
    print(grouped_data)