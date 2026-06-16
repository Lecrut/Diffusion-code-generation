def find_max_value(numbers):
    if not numbers:
        return None
    max_val = float('-inf')
    for num in numbers:
        try:
            val = float(num)
        except (TypeError, ValueError):
            raise TypeError(f"All elements must be numeric. Found {type(num).__name__} at index.") from None
        if val > max_val:
            max_val = val
    return int(max_val) if isinstance(numbers[0], (int, float)) and not isinstance(float('inf'), type(val)) else max_val
if __name__ == '__main__':
    sample_data = [12.5, 45, -9, 78.3, 2]
    result = find_max_value(sample_data)
    print(f"Maximum value: {result}")
    empty_list = []
    max_empty = find_max_value(empty_list)
    if max_empty is None:
        print("Empty list handled correctly.")