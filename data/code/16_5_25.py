def determine_positivity(num):
    if num > 0:
        return 'positive'
    elif num < 0:
        return 'negative'
    else:
        return 'zero'
assert determine_positivity(10) == 'positive'
assert determine_positivity(-5) == 'negative'
assert determine_positivity(0) == 'zero'
if __name__ == '__main__':
    sample_values = [10, -5, 0]
    for value in sample_values:
        print(determine_positivity(value))