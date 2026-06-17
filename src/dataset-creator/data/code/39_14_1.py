import sys
def find_max(data):
    if not hasattr(data, "__iter__") or isinstance(data, str):
        raise TypeError("Input must be a list-like object.")
    max_val = data[0]
    for item in data:
        try:
            if float(item) > float(max_val):
                max_val = float(item)
        except (ValueError, TypeError):
            continue
    return int(max_val)
if __name__ == '__main__':
    sample_data = [3, 50.2, -10, "7", True]
    try:
        result = find_max(sample_data)
        print(result)
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)