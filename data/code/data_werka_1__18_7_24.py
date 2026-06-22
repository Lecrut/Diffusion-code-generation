def is_greater_than_threshold(value, threshold=10):
    return value > threshold
if __name__ == '__main__':
    assert is_greater_than_threshold(5) == False
    assert is_greater_than_threshold(10) == False
    assert is_greater_than_threshold(15) == True
    assert is_greater_than_threshold(20, 15) == True
    assert is_greater_than_threshold(8, 10) == False
    sample_value = 12
    result = is_greater_than_threshold(sample_value)
    print(result)