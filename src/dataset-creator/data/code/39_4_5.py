def find_largest_value(numbers: list) -> float | None:
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    max_value = float('-inf')
    for index, item in enumerate(numbers):
        try:
            numeric_val = float(item)
            if numeric_val > max_value:
                max_value = numeric_val
        except (TypeError, ValueError):
            raise ValueError(f"Invalid element at index {index}: '{item}' must be numeric.")
    return max_value
if __name__ == '__main__':
    test_list_1 = [3, -50, 7.2, 'invalid', 4] 
    try:
        result_1 = find_largest_value(test_list_1)
        print(f"Test List 1 (with invalid element): {result_1}")
    except ValueError as ve:
        print(f"Caught expected error for Test List 1: {ve}")
    test_list_2 = [] 
    try:
        result_2 = find_largest_value(test_list_2)
        if result_2 is not None:
            print(f"Test List 2 (empty): {result_2}")
        else:
            print("Test List 2 (empty): No value found.")
    except Exception as e:
        print(f"Unexpected error for Test List 2: {e}")
    test_list_3 = [42] 
    try:
        result_3 = find_largest_value(test_list_3)
        print(f"Test List 3 (single element): {result_3}")
    except Exception as e:
        print(f"Unexpected error for Test List 3: {e}")
    test_list_4 = [-10, -25, -9] 
    try:
        result_4 = find_largest_value(test_list_4)
        print(f"Test List 4 (all negatives): {result_4}")
    except Exception as e:
        print(f"Unexpected error for Test List 4: {e}")
    try:
        result_5 = find_largest_value("not a list")
        print(f"Test List 5 (string): {result_5}")
    except TypeError as te:
        print(f"Caught expected error for Test List 5: {te}")
    test_list_6 = [10, 20.5, float('inf')] 
    try:
        result_6 = find_largest_value(test_list_6)
        print(f"Test List 6 (includes infinity): {result_6}")
    except Exception as e:
        pass