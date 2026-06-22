def is_valid_string(item):
    return isinstance(item, str)

def print_items(data):
    for item in data:
        if is_valid_string(item):
            print(item)

if __name__ == '__main__':
    sample_items = [
        "Apple",
        "Banana",
        "Cherry",
        123,
        "Date"
    ]
    print_items(sample_items)