import sys
def get_head(safe_list):
    if not safe_list:
        raise ValueError("The provided collection is empty.")
    return safe_list[0]
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    try:
        head_element = get_head(sample_data)
        print(f"Head element retrieved successfully: {head_element}")
    except ValueError as e:
        error_message = f"{type(e).__name__}: {e}"
        sys.stderr.write(error_message + "\n")
        sys.exit(1)
    empty_collection = []
    try:
        head_empty = get_head(empty_collection)
    except ValueError as e:
        print(f"Expected error for empty list caught correctly.")