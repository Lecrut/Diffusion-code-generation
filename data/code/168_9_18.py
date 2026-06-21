from collections import defaultdict

def group_by_keys(data, *keys):
    result = defaultdict(dict)
    for item in data:
        current_level = result
        for key in keys[:-1]:
            if key not in current_level:
                current_level[key] = defaultdict(dict)
            current_level = current_level[key]
        last_key = keys[-1]
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
    grouped = group_by_keys(data, 'a', 'b')
    print(grouped)