import sys
def read_and_print_items(input_data):
    for item in input_data:
        print(item)
if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", 123, "date"]
    try:
        read_and_print_items(sample_items)
    except Exception as e:
        print(f"An error occurred during processing: {e}", file=sys.stderr)