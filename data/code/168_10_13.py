from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'fruit', 'name': 'apple'},
        {'id': 2, 'category': 'fruit', 'name': 'banana'},
        {'id': 3, 'category': 'vegetable', 'name': 'carrot'}
    ]
    key_to_group_by = 'category'
    result = group_by_key(sample_data, key_to_group_by)
    print(result)