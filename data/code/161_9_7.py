def validate_input(items):
    if not isinstance(items, dict) or not all(isinstance(k, str) for k in items.keys()):
        raise ValueError("Input must be a dictionary with string keys")

def get_sorted_item_names(items):
    validate_input(items)
    return sorted(items.keys())

if __name__ == '__main__':
    sample_items = {
        'apple': 3,
        'banana': 2,
        'cherry': 5,
        'date': 4
    }
    sorted_items = get_sorted_item_names(sample_items)
    print(sorted_items)