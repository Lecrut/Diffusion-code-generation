import sys
def process_input(data):
    for item in data:
        print(item)
if __name__ == '__main__':
    sample_items = [
        "Apple",
        "Banana",
        "Cherry",
        123,
        "Date",
        "",
        3.14
    ]
    valid_items = []
    for item in sample_items:
        try:
            if isinstance(item, str):
                valid_items.append(item)
            elif isinstance(item, int) or isinstance(item, float):
                valid_items.append(str(item))
            else:
                print(f"Error: Invalid data type encountered: {item}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing item '{item}': {e}", file=sys.stderr)
    process_input(valid_items)