from collections import defaultdict

def group_by_key(data, key):
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Data must be a list of dictionaries.")
    
    grouped = defaultdict(list)
    for item in data:
        if key not in item:
            raise KeyError(f"Key '{key}' not found in dictionary.")
        grouped[item[key]].append(item)
    return dict(grouped)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'category': 'fruit', 'name': 'apple'},
        {'id': 2, 'category': 'vegetable', 'name': 'carrot'},
        {'id': 3, 'category': 'fruit', 'name': 'banana'},
        {'id': 4, 'category': 'meat', 'name': 'chicken'}
    ]
    
    try:
        grouped_data = group_by_key(sample_data, 'category')
        print(grouped_data)
    except (ValueError, KeyError) as e:
        print(e)