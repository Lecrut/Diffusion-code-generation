def determine_positivity(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'
if __name__ == '__main__':
    assert determine_positivity(10) == 'Positive', 'Test failed for positive number'
    assert determine_positivity(-5) == 'Negative', 'Test failed for negative number'
    assert determine_positivity(0) == 'Zero', 'Test failed for zero'
    print(determine_positivity(10))
    print(determine_positivity(-5))
    print(determine_positivity(0))