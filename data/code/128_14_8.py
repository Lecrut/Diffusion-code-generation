def is_negative(value):
    return value < 0

if __name__ == '__main__':
    test_values = [1, -2, 3.5, -4.5]
    expected_results = [False, True, False, True]
    
    for value, expected in zip(test_values, expected_results):
        result = is_negative(value)
        assert result == expected, f"Test Failed: Expected {expected}, Got {result} for value {value}"
        print(f"Value {value}: {'Negative' if result else 'Non-negative'}")