def is_greater_than_threshold(value, threshold=10):
    return value > threshold
if __name__ == '__main__':
    test_value_1 = 5
    test_value_2 = 15
    test_value_3 = 10
    assert not is_greater_than_threshold(test_value_1), 'Test case 1 failed'
    assert is_greater_than_threshold(test_value_2), 'Test case 2 failed'
    assert not is_greater_than_threshold(test_value_3), 'Test case 3 failed'
    print(is_greater_than_threshold(20))
    print(is_greater_than_threshold(5))