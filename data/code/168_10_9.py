from collections import defaultdict

def group_by_key(items, key):
    grouped = defaultdict(list)
    for item in items:
        if key in item:
            grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_items = [
        {'id': 1, 'category': 'fruit'},
        {'id': 2, 'category': 'vegetable'},
        {'id': 3, 'category': 'fruit'},
        {'id': 4, 'category': 'fruit'},
        {'id': 5, 'category': 'vegetable'}
    ]
    
    grouped_items = group_by_key(sample_items, 'category')
    for category, items in grouped_items.items():
        print(f"{category}: {items}")