from collections import defaultdict

def group_by_key(data, key):
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All items in the data list must be dictionaries.")
    if not isinstance(key, str):
        raise ValueError("The key must be a string.")
    
    grouped = defaultdict(list)
    for item in data:
        grouped[item.get(key, None)].append(item)
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