def validate_items(item_list):
    if not isinstance(item_list, list):
        raise ValueError("Input must be a list")
    for item in item_list:
        if not isinstance(item, str):
            raise ValueError("All items in the list must be strings")

def print_items(items):
    validate_items(items)
    for item in items:
        print(item)

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    print_items(sample_items)