from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'fruit'},
        {'id': 2, 'category': 'vegetable'},
        {'id': 3, 'category': 'fruit'},
        {'id': 4, 'category': 'meat'}
    ]
    result = group_by_key(sample_data, 'category')
    print(result)