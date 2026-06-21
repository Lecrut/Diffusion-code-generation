def group_by_keys(data, *keys):
    result = {}
    for item in data:
        current_level = result
        for key in keys[:-1]:
            if item[key] not in current_level:
                current_level[item[key]] = {}
            current_level = current_level[item[key]]
        last_key = keys[-1]
        if item[last_key] not in current_level:
            current_level[item[last_key]] = []
        current_level[item[last_key]].append(item)
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