def validate_items(items):
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All items must be strings")
    return items

def print_items(items):
    for item in items:
        print(item)

if __name__ == '__main__':
    sample_items = validate_items(['apple', 'banana', 'cherry'])
    print_items(sample_items)