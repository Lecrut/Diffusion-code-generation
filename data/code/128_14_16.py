def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [1, -2, 3, -4, 5]
    expected_results = [False, True, False, True, False]
    
    for i, val in enumerate(test_values):
        result = is_negative(val)
        assert result == expected_results[i], f"Test {i+1} Failed: Expected {expected_results[i]}, Got {result}"
        print(f"Test {i+1} Passed: {val} -> {result}")