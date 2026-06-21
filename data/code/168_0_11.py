from collections import defaultdict

def group_by_key(items, key):
    groups = defaultdict(list)
    for item in items:
        groups[item[key]].append(item)
    return dict(groups)

if __name__ == '__main__':
    sample_items = [
        {'type': 'fruit', 'name': 'apple'},
        {'type': 'vegetable', 'name': 'carrot'},
        {'type': 'fruit', 'name': 'banana'},
        {'type': 'dairy', 'name': 'milk'}
    ]
    grouped_items = group_by_key(sample_items, 'type')
    print(grouped_items)