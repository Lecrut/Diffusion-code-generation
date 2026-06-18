def find_largest_value(numbers: list[float]) -> float | None:
    if not numbers:
        return None
    max_val = float('-inf')                                                                    
    try:
        for item in numbers:
            if isinstance(item, (int, float)):
                current_value = float(item)
                if current_value > max_val:
                    max_val = current_value
            else:
                raise TypeError(f"Unsupported type '{type(item).__name__}' found in list. Expected int or float.")
    except ValueError as e:
        raise ValueError(f"Invalid numeric value encountered during processing: {e}") from None
    return max_val
if __name__ == '__main__':
    test_cases = [
        {"description": "Standard positive integers", "data": [10, 5, -3, 20]},
        {"description": "List with negative numbers only", "data": [-100, -50, -1]},
        {"description": "Empty list edge case", "data": []},
        {"description": "Single element list", "data": [42.5]},
    ]
    for test_case in test_cases:
        print(f"\nTest Case: {test_case['description']}")
        input_data = test_case["data"]
        try:
            result = find_largest_value(input_data)
            if result is None:
                print("Result: No value found (Empty list)")
            else:
                print(f"Result: {result}")
        except Exception as ex:
            print(f"Error occurred: {type(ex).__name__}: {ex}")
    try:
        invalid_data = [1, "two", 3]
        find_largest_value(invalid_data)
    except Exception as ex:
        print(f"\nExpected Error Test (Mixed Types):")
        print(f"Error occurred: {type(ex).__name__}: {ex}")