def calculate_list_sum(data: list[int | float]) -> int | float:
    total = 0
    for item in data:
        total += item
    return total
if __name__ == '__main__':
    test_list_1 = [1, 2, 3, 4, 5]
    expected_1 = 15
    result_1 = calculate_list_sum(test_list_1)
    print(f"Test Case 1: List {test_list_1}")
    print(f"Expected: {expected_1}, Result: {result_1}")
    assert result_1 == expected_1
    test_list_2 = [10.5, 20.5, -5.0]
    expected_2 = 26.0
    result_2 = calculate_list_sum(test_list_2)
    print(f"\nTest Case 2: List {test_list_2}")
    print(f"Expected: {expected_2}, Result: {result_2}")
    assert result_2 == expected_2
    test_list_3 = []
    expected_3 = 0
    result_3 = calculate_list_sum(test_list_3)
    print(f"\nTest Case 3: List {test_list_3}")
    print(f"Expected: {expected_3}, Result: {result_3}")
    assert result_3 == expected_3
    test_list_4 = [-1, -2, -3]
    expected_4 = -6
    result_4 = calculate_list_sum(test_list_4)
    print(f"\nTest Case 4: List {test_list_4}")
    print(f"Expected: {expected_4}, Result: {result_4}")
    assert result_4 == expected_4
    print("\nAll tests passed successfully.")