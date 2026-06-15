def calculate_list_sum(data):
    total = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
    return total
if __name__ == '__main__':
    test_list_1 = [1, 2, 3, 4, 5]
    expected_sum_1 = 15
    actual_sum_1 = calculate_list_sum(test_list_1)
    print(f"Test Case 1: List {test_list_1}")
    print(f"Expected: {expected_sum_1}, Actual: {actual_sum_1}")
    assert actual_sum_1 == expected_sum_1
    test_list_2 = [10, -5, 2.5, 0]
    expected_sum_2 = 7.5
    actual_sum_2 = calculate_list_sum(test_list_2)
    print(f"Test Case 2: List {test_list_2}")
    print(f"Expected: {expected_sum_2}, Actual: {actual_sum_2}")
    assert actual_sum_2 == expected_sum_2
    test_list_3 = []
    expected_sum_3 = 0
    actual_sum_3 = calculate_list_sum(test_list_3)
    print(f"Test Case 3: List {test_list_3}")
    print(f"Expected: {expected_sum_3}, Actual: {actual_sum_3}")
    assert actual_sum_3 == expected_sum_3
    test_list_4 = ["a", "b", 10]
    expected_sum_4 = 10
    actual_sum_4 = calculate_list_sum(test_list_4)
    print(f"Test Case 4: List {test_list_4}")
    print(f"Expected: {expected_sum_4}, Actual: {actual_sum_4}")
    assert actual_sum_4 == expected_sum_4
    print("All tests passed.")