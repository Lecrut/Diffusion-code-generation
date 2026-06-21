def group_by(iterable, key_func):
    current_key = None
    current_group = []
    
    for item in iterable:
        key = key_func(item)
        if key != current_key:
            if current_group:
                yield current_key, current_group
            current_key = key
            current_group = [item]
        else:
            current_group.append(item)
    
    if current_group:
        yield current_key, current_group

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'fruit'},
        {'id': 2, 'category': 'vegetable'},
        {'id': 3, 'category': 'fruit'},
        {'id': 4, 'category': 'meat'}
    ]
    
    for category, items in group_by(sample_data, lambda x: x['category']):
        print(f"Category: {category}")
        for item in items:
            print(item)