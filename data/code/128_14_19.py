def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_value_1 = -3
    result_1 = is_negative(test_value_1)
    assert result_1, f"Test 1 Failed: Expected True, Got {result_1}"
    print("Test 1 Passed")

    test_value_2 = 4
    result_2 = is_negative(test_value_2)
    assert not result_2, f"Test 2 Failed: Expected False, Got {result_2}"
    print("Test 2 Passed")