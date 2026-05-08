def check_negativity(data: list[int]) -> list[bool]:
    return [x < 0 for x in data]
if __name__ == '__main__':
    test_list_1 = [1, -2, 3, -4, 5]
    expected_1 = [False, True, False, True, False]
    result_1 = check_negativity(test_list_1)
    print(f"Input: {test_list_1}")
    print(f"Result: {result_1}")
    print(f"Expected: {expected_1}")
    assert result_1 == expected_1
    test_list_2 = [10, 20, 30]
    expected_2 = [False, False, False]
    result_2 = check_negativity(test_list_2)
    print(f"\nInput: {test_list_2}")
    print(f"Result: {result_2}")
    print(f"Expected: {expected_2}")
    assert result_2 == expected_2
    test_list_3 = [-1, -5, 0, 100]
    expected_3 = [True, True, False, False]
    result_3 = check_negativity(test_list_3)
    print(f"\nInput: {test_list_3}")
    print(f"Result: {result_3}")
    print(f"Expected: {expected_3}")
    assert result_3 == expected_3
    print("\nAll tests passed.")