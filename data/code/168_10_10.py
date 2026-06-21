from collections import defaultdict

def group_by_key(items, key):
    if not all(isinstance(item, dict) for item in items):
        raise ValueError("All items must be dictionaries")
    if not callable(key):
        raise ValueError("Key must be a callable function")

    grouped = defaultdict(list)
    for item in items:
        k = key(item)
        grouped[k].append(item)

    return dict(grouped)

if __name__ == '__main__':
    sample_items = [
        {'id': 1, 'category': 'fruit'},
        {'id': 2, 'category': 'vegetable'},
        {'id': 3, 'category': 'fruit'},
        {'id': 4, 'category': 'meat'}
    ]
    
    try:
        grouped_items = group_by_key(sample_items, lambda x: x['category'])
        print(grouped_items)
    except ValueError as e:
        print(e)