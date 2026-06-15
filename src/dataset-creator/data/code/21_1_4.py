def group_by_field(data, field):
    result = {}
    for item in data:
        key = item[field]
        if key is not None:
            if key not in result:
                result[key] = []
            result[key].append(item)
    return result
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'A', 'value': 10},
        {'id': 2, 'category': 'B', 'value': 20},
        {'id': 3, 'category': 'A', 'value': 30},
        {'id': 4, 'category': 'C', 'value': 40},
        {'id': 5, 'category': 'B', 'value': 50}
    ]
    field_to_group_by = 'category'
    grouped_data = group_by_field(sample_data, field_to_group_by)
    print(grouped_data)