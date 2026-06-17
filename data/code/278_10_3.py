import sys
def read_and_print_items(input_data):
    for item in input_data:
        print(item)
if __name__ == '__main__':
    sample_input = [
        "Apple",
        "Banana",
        "Cherry",
        123,
        "Date"
    ]
    valid_items = []
    for item in sample_input:
        try:
            if isinstance(item, str):
                valid_items.append(item)
            else:
                print(f"Error: Invalid data type encountered: {item}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing item '{item}': {e}", file=sys.stderr)
    read_and_print_items(valid_items)