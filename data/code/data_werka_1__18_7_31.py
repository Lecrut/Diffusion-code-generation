def is_above_threshold(value, threshold=10):
    return value > threshold
if __name__ == '__main__':
    test_cases = [(5, 10), (15, 10), (20, 10), (8, 10), (10, 10)]
    for value, threshold in test_cases:
        result = is_above_threshold(value, threshold)
        print(f'is_above_threshold({value}, {threshold}) = {result}')
    assert is_above_threshold(5, 10) == False
    assert is_above_threshold(15, 10) == True
    assert is_above_threshold(20, 10) == True
    assert is_above_threshold(8, 10) == False
    assert is_above_threshold(10, 10) == False
    print('All test cases passed.')