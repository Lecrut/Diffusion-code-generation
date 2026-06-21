def find_min_max(data):
    if not data:
        return None, None
    try:
        minimum = min(data)
        maximum = max(data)
        return minimum, maximum
    except TypeError:
        raise ValueError("Input list must contain only integers") from None

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")

    sample_list_empty = []
    try:
        min_val_empty, max_val_empty = find_min_max(sample_list_empty)
        print(f"Empty list Min: {min_val_empty}, Max: {max_val_empty}")
    except ValueError as e:
        print(e)

    sample_list_with_invalid = [3, 1, 'a', 5]
    try:
        min_val_invalid, max_val_invalid = find_min_max(sample_list_with_invalid)
        print(f"Invalid list Min: {min_val_invalid}, Max: {max_val_invalid}")
    except ValueError as e:
        print(e)