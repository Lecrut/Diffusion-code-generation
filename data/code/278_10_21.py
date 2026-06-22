def print_items(item_list):
    for item in item_list:
        if isinstance(item, str):
            print(item)
        else:
            raise ValueError(f"Non-string value encountered: {item}")

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
        print(f"An error occurred during processing: {e}", file=sys.stderr)