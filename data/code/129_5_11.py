def group_and_sort(objects, group_attr, sort_attr):
    from collections import defaultdict

    grouped = defaultdict(list)
    for obj in objects:
        grouped[obj[group_attr]].append(obj)

    sorted_groups = {key: sorted(group, key=lambda x: x[sort_attr], reverse=True) for key, group in grouped.items()}
    return dict(sorted_groups)

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