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
        {'type': 'fruit', 'color': 'red', 'name': 'apple'},
        {'type': 'fruit', 'color': 'green', 'name': 'banana'},
        {'type': 'vegetable', 'color': 'yellow', 'name': 'carrot'},
        {'type': 'fruit', 'color': 'red', 'name': 'cherry'}
    ]
    print(group_by_keys(sample_data, 'type', 'color'))