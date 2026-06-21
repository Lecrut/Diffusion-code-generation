from collections import defaultdict

def group_by_key(items, key):
    grouped_items = defaultdict(list)
    for item in items:
        grouped_items[item[key]].append(item)
    return dict(grouped_items)

if __name__ == '__main__':
    sample_items = [
        {'type': 'fruit', 'name': 'apple'},
        {'type': 'vegetable', 'name': 'carrot'},
        {'type': 'fruit', 'name': 'banana'},
        {'type': 'dairy', 'name': 'milk'},
        {'type': 'fruit', 'name': 'orange'}
    ]
    grouped = group_by_key(sample_items, 'type')
    print(grouped)