def find_largest_value(numbers: list[float]) -> float | None:
    max_val = float('-inf')
    for item in numbers:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Expected int or float, got {type(item).__name__}")
        current_value = float(item)                                                    
        if current_value > max_val:
            max_val = current_value
    return max_val
if __name__ == '__main__':
    test_list_1 = [30, 50, -20, 75]
    test_list_2 = [-100, -50, -99]
    test_list_3 = []
    test_list_4 = [42]
    print(f"Largest in {test_list_1}:")
    result_1 = find_largest_value(test_list_1)
    if result_1 is not None:
        print(result_1)
    print("\nLargest in negative numbers:")
    result_2 = find_largest_value(test_list_2)
    if result_2 is not None:
        print(result_2)
    print("\nLargest in empty list (should be handled gracefully):")
    try:
        result_3 = find_largest_value(test_list_3)
        if result_3 is not None:
            print(result_3)
        else:
            print("No valid numbers found.")
    except Exception as e:
        print(f"Error occurred: {e}")
    print("\nLargest in single element:")
    result_4 = find_largest_value(test_list_4)
    if result_4 is not None:
        print(result_4)