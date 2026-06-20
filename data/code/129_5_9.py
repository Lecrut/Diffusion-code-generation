from collections import defaultdict

def group_and_sort(objects, group_key, sort_key):
    grouped = defaultdict(list)
    for obj in objects:
        grouped[obj[group_key]].append(obj)
    
    for key, items in grouped.items():
        grouped[key] = sorted(items, key=lambda x: x[sort_key], reverse=True)
    
    return dict(grouped)

if __name__ == '__main__':
    objects = [
        {'category': 'A', 'value': 3},
        {'category': 'B', 'value': 1},
        {'category': 'A', 'value': 2},
        {'category': 'B', 'value': 4}
    ]
    
    result = group_and_sort(objects, 'category', 'value')
    print(result)