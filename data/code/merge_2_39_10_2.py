def find_largest_item(items):
    if not items:
        raise ValueError("Error: The provided list is empty.")
    max_value = float('-inf')
    for item in items:
        try:
            numeric_val = float(item)
            if numeric_val > max_value:
                max_value = numeric_val
        except (ValueError, TypeError):
            raise ValueError(f"Error: Invalid type '{item}' found in the list. All elements must be numbers.")
    return int(max_value)
if __name__ == '__main__':
    sample_list = [10, 25, -3, '4', None]
    try:
        result = find_largest_item(sample_list)
        print(f"The largest item is {result}.")
    except ValueError as e:
        print(e)