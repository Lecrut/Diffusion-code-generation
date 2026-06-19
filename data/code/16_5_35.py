def determine_positivity(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'
assert determine_positivity(10) == 'Positive', 'Test case for positive number failed'
assert determine_positivity(-5) == 'Negative', 'Test case for negative number failed'
assert determine_positivity(0) == 'Zero', 'Test case for zero failed'
if __name__ == '__main__':
    print(determine_positivity(10))
    print(determine_positivity(-5))
    print(determine_positivity(0))