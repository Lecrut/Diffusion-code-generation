def is_greater_than_threshold(value, threshold=10):
    return value > threshold
if __name__ == '__main__':
    test_values = [5, 10, 15, 20]
    for value in test_values:
        result = is_greater_than_threshold(value)
        print(f'{value} > 10: {result}')
    assert is_greater_than_threshold(5) == False
    assert is_greater_than_threshold(10) == False
    assert is_greater_than_threshold(15) == True
    assert is_greater_than_threshold(20) == True