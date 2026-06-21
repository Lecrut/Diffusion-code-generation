from collections import defaultdict

def validate_input(data, key):
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All items must be dictionaries.")
    if not any(key in item for item in data):
        raise KeyError(f"Key '{key}' not found in any dictionary.")

def group_by_key(data, key):
    validate_input(data, key)
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'fruit', 'name': 'apple'},
        {'id': 2, 'category': 'vegetable', 'name': 'carrot'},
        {'id': 3, 'category': 'fruit', 'name': 'banana'},
        {'id': 4, 'category': 'meat', 'name': 'chicken'}
    ]
    grouped_data = group_by_key(sample_data, 'category')
    print(grouped_data)