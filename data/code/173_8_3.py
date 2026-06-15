import collections
def group_by_string(data):
    groups = collections.defaultdict(list)
    for item in data:
        key = item['string_attribute']
        groups[key].append(item)
    return dict(groups)
if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'string_attribute': 'A', 'value': 10},
        {'id': 2, 'string_attribute': 'B', 'value': 20},
        {'id': 3, 'string_attribute': 'A', 'value': 15},
        {'id': 4, 'string_attribute': 'C', 'value': 30},
        {'id': 5, 'string_attribute': 'B', 'value': 25},
        {'id': 6, 'string_attribute': 'A', 'value': 12},
    ]
    grouped_data = group_by_string(sample_data)
    print(grouped_data)