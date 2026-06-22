def validate_items(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    for item in items:
        if not isinstance(item, str):
            raise ValueError("All items in the list must be strings")

def print_list(items):
    validate_items(items)
    for item in items:
        print(item)

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    print_list(sample_items)