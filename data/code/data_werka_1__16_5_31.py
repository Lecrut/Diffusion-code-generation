def determine_positivity(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'
assert determine_positivity(10) == 'Positive'
assert determine_positivity(-5) == 'Negative'
assert determine_positivity(0) == 'Zero'
if __name__ == '__main__':
    print(determine_positivity(23))
    print(determine_positivity(-17))
    print(determine_positivity(0))