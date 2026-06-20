def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [1, -2, 3, -4, 5, 10, 20, 30, -1, -5, 0]
    expected_results = [False, True, False, True, False, False, False, False, True, True, False]

    for value, expected in zip(test_values, expected_results):
        result = is_negative(value)
        assert result == expected, f"Test Failed: Expected {expected}, Got {result} for value {value}"
    
    print("All tests passed")