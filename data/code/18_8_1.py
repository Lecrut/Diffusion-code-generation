def is_greater_than_threshold(value, threshold):
    return value > threshold
if __name__ == '__main__':
    test_value_1 = 10
    test_threshold_1 = 5
    assert is_greater_than_threshold(test_value_1, test_threshold_1) == True
    test_value_2 = 3
    test_threshold_2 = 5
    assert is_greater_than_threshold(test_value_2, test_threshold_2) == False
    test_value_3 = 5
    test_threshold_3 = 5
    assert is_greater_than_threshold(test_value_3, test_threshold_3) == False
    test_value_4 = 11
    test_threshold_4 = 10
    assert is_greater_than_threshold(test_value_4, test_threshold_4) == True
    test_value_5 = -1
    test_threshold_5 = -5
    assert is_greater_than_threshold(test_value_5, test_threshold_5) == True
    test_value_6 = 0
    test_threshold_6 = 0
    assert is_greater_than_threshold(test_value_6, test_threshold_6) == False
    print("All test cases passed!")