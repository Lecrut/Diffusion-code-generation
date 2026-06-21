def validate_items(items):
    if not isinstance(items, dict) or not all(isinstance(k, str) for k in items.keys()):
        raise ValueError("Items must be a dictionary with string keys")

def get_sorted_item_names():
    items = {
        'apple': 3,
        'banana': 2,
        'cherry': 5,
        'date': 4
    }
    validate_items(items)
    sorted_items = sorted(items.keys())
    return sorted_items

if __name__ == '__main__':
    print(get_sorted_item_names())