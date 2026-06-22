def validate_items(data):
    valid_items = []
    for item in data:
        if isinstance(item, str) and item.strip():
            valid_items.append(item)
    return valid_items

def print_items(items):
    for item in items:
        print(item)

if __name__ == '__main__':
    sample_items = [
        "Apple",
        "Banana",
        "Cherry",
        123,
        "Date",
        "",
        None
    ]
    valid_items = validate_items(sample_items)
    print_items(valid_items)