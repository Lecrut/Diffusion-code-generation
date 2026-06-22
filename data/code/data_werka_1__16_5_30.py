def determine_positivity(num):
    if num > 0:
        return 'positive'
    elif num < 0:
        return 'negative'
    else:
        return 'zero'
assert determine_positivity(10) == 'positive', 'Test case 1 failed'
assert determine_positivity(-5) == 'negative', 'Test case 2 failed'
assert determine_positivity(0) == 'zero', 'Test case 3 failed'
if __name__ == '__main__':
    print(determine_positivity(10))
    print(determine_positivity(-5))
    print(determine_positivity(0))