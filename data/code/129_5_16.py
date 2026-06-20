def group_and_sort(objects, group_attr, sort_attr):
    from collections import defaultdict
    groups = defaultdict(list)
    for obj in objects:
        groups[obj[group_attr]].append(obj)
    for key, group in groups.items():
        groups[key] = sorted(group, key=lambda x: x[sort_attr], reverse=True)
    return dict(groups)

if __name__ == '__main__':
    sample_objects = [
        {'category': 'A', 'value': 3},
        {'category': 'B', 'value': 1},
        {'category': 'A', 'value': 2},
        {'category': 'B', 'value': 4}
    ]
    result = group_and_sort(sample_objects, 'category', 'value')
    print(result)