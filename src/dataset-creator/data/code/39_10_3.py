def find_largest_item(items):
    if not items:
        raise ValueError("Error: The list is empty and cannot contain a largest item.")
    max_value = float('-inf')
    for i in range(len(items)):
        current_val = items[i]
        try:
            numeric_current = float(current_val)
            if numeric_current > max_value:
                max_value = numeric_current
        except ValueError as e:
            raise TypeError(f"Error: List contains non-numeric values. Invalid item at index {i}: {current_val}.") from e
    return int(max_value)
if __name__ == '__main__':
    sample_list = [5, 12, -3, 89, 4]
    try:
        result = find_largest_item(sample_list)
        print(f"The largest item in the list is: {result}")
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)