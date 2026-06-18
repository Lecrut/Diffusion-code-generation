import sys
def get_head(safe_list):
    if not safe_list:
        raise ValueError("Collection is empty")
    return safe_list[0]
if __name__ == '__main__':
    sample_data = [1, 2, 3]
    try:
        result = get_head(sample_data)
        print(f"Head value: {result}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)