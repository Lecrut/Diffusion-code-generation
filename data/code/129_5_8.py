def group_and_sort(objects, group_key, sort_key):
    from collections import defaultdict
    groups = defaultdict(list)
    for obj in objects:
        groups[obj[group_key]].append(obj)
    for key, group in groups.items():
        groups[key] = sorted(group, key=lambda x: x[sort_key], reverse=True)
    return dict(groups)

if __name__ == '__main__':
    sample_objects = [
        {'category': 'A', 'value': 3},
        {'category': 'B', 'value': 1},
        {'category': 'A', 'value': 2},
        {'category': 'C', 'value': 4},
        {'category': 'B', 'value': 5}
    ]
    result = group_and_sort(sample_objects, 'category', 'value')
    print(result)