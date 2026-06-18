import sys
def get_head(safe_list):
    try:
        if not safe_list:
            raise IndexError("List is empty")
        return safe_list[0]
    except Exception as e:
        print(f"Error retrieving head: {e}", file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    sample_data = [42, "hello", 3.14]
    try:
        result = get_head(sample_data)
        print("Head element:", result)
    except IndexError as e:
        print(f"Error retrieving head: {e}", file=sys.stderr)