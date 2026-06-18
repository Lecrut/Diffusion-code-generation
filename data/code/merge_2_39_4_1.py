def find_largest_value(numbers: list[float]) -> float | None:
    if not numbers:
        return None
    try:
        max_val = float(numbers[0])
        for num in numbers[1:]:
            if isinstance(num, (int, float)):
                current_max = float(max_val)
                if num > current_max:
                    max_val = num
        return max_val
    except TypeError as e:
        raise TypeError(f"List contains non-numeric elements. Error details: {e}")
if __name__ == '__main__':
    test_data_1 = [3, 7, -2, 9.5, 4]
    test_data_empty = []
    print(f"Largest in {test_data_1}:")
    result_1 = find_largest_value(test_data_1)
    if result_1 is not None:
        print(result_1)
    else:
        print("No value found.")
    print("\nLargest in empty list:")
    result_empty = find_largest_value(test_data_empty)
    print(f"Result: {result_empty}")