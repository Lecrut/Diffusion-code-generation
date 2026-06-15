def group_objects(data, key_path):
    groups = {}
    for item in data:
        current_key = None
        temp = item
        path_parts = key_path.split('.')
        found = True
        for part in path_parts:
            if isinstance(temp, dict) and part in temp:
                temp = temp[part]
                current_key = part
            else:
                found = False
                break
        if found:
            group_key = temp
            if group_key not in groups:
                groups[group_key] = []
            groups[group_key].append(item)
    return groups
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'A', 'details': {'type': 'X', 'value': 10}},
        {'id': 2, 'category': 'B', 'details': {'type': 'Y', 'value': 20}},
        {'id': 3, 'category': 'A', 'details': {'type': 'Z', 'value': 30}},
        {'id': 4, 'category': 'C'},
        {'id': 5, 'category': 'B', 'details': {'type': 'X', 'value': 40}},
        {'id': 6, 'other_field': 'test'}
    ]
    key = 'category.details.type'
    result = group_objects(sample_data, key)
    print(result)