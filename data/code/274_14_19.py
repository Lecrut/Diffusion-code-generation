def validate_items(item_list):
    if not all(isinstance(item, str) for item in item_list):
        raise ValueError("All items must be strings")
    if len(item_list) == 0:
        raise ValueError("Item list cannot be empty")

def print_items(items):
    validate_items(items)
    for item in items:
        print(item)

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    print_items(sample_items)