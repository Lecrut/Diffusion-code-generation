def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_value_1 = -7
    expected_1 = True
    result_1 = is_negative(test_value_1)
    assert result_1 == expected_1, f"Test 1 Failed: Expected {expected_1}, Got {result_1}"
    print("Test 1 Passed")

    test_value_2 = 3.5
    expected_2 = False
    result_2 = is_negative(test_value_2)
    assert result_2 == expected_2, f"Test 2 Failed: Expected {expected_2}, Got {result_2}"
    print("Test 2 Passed")

    test_value_3 = -0.1
    expected_3 = True
    result_3 = is_negative(test_value_3)
    assert result_3 == expected_3, f"Test 3 Failed: Expected {expected_3}, Got {result_3}"
    print("Test 3 Passed")