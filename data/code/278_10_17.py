def print_items(item_list):
    for item in item_list:
        if not isinstance(item, str):
            raise ValueError(f"Invalid input: {item} is not a string")
        print(item)

if __name__ == '__main__':
    sample_items = [
        "Apple",
        "Banana",
        "Cherry",
        123,
        "Date"
    ]
    try:
        print_items(sample_items)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)