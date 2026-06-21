def group_by_key(iterable, key_func):
    current_group = None
    current_key = None
    for item in iterable:
        new_key = key_func(item)
        if new_key != current_key:
            if current_group is not None:
                yield current_group
            current_group = []
            current_key = new_key
        current_group.append(item)
    if current_group is not None:
        yield current_group

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'A'},
        {'id': 2, 'category': 'B'},
        {'id': 3, 'category': 'A'},
        {'id': 4, 'category': 'C'},
        {'id': 5, 'category': 'B'}
    ]
    for group in group_by_key(sample_data, lambda x: x['category']):
        print(group)