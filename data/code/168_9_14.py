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
        {'id': 1, 'type': 'fruit', 'color': 'red'},
        {'id': 2, 'type': 'fruit', 'color': 'green'},
        {'id': 3, 'type': 'vegetable', 'color': 'yellow'},
        {'id': 4, 'type': 'fruit', 'color': 'red'},
        {'id': 5, 'type': 'vegetable', 'color': 'green'}
    ]
    
    grouped_data = group_by_keys(sample_data, 'type', 'color')
    print(grouped_data)