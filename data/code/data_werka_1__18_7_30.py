def is_value_greater_than_threshold(value, threshold=10):
    return value > threshold
if __name__ == '__main__':
    test_cases = [(5, 10), (15, 10), (20, 20), (30, 25)]
    for value, threshold in test_cases:
        result = is_value_greater_than_threshold(value, threshold)
        print(f'is_value_greater_than_threshold({value}, {threshold}) = {result}')
    assert is_value_greater_than_threshold(5, 10) == False
    assert is_value_greater_than_threshold(15, 10) == True
    assert is_value_greater_than_threshold(20, 20) == False
    assert is_value_greater_than_threshold(30, 25) == True