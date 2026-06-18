def find_largest_element(data):
    if not data:
        raise ValueError("Input list cannot be empty.")
    for i, item in enumerate(data):
        try:
            num = float(item)
        except TypeError as e:
            raise TypeError(f"Invalid type at index {i}: expected numeric value, got {type(item).__name__}.") from e
        if not isinstance(num, (int, float)):
            continue
    max_val = data[0]
    for item in data:
        try:
            num = float(item)
            if num > max_val:
                max_val = num
        except TypeError as e:
            raise ValueError(f"Cannot process element at index {i}: invalid type.") from e
    return int(max_val)
if __name__ == '__main__':
    sample_list = [10, "25", 3.7, None]
    try:
        result = find_largest_element(sample_list)
        print(f"Largest element: {result}")
    except (ValueError, TypeError) as e:
        print(f"Error occurred: {e}")