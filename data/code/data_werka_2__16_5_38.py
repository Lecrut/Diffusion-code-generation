def determine_positivity(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'
assert determine_positivity(10) == 'Positive', 'Test case 1 failed'
assert determine_positivity(-5) == 'Negative', 'Test case 2 failed'
assert determine_positivity(0) == 'Zero', 'Test case 3 failed'
if __name__ == '__main__':
    sample_values = [42, -17, 0]
    for value in sample_values:
        result = determine_positivity(value)
        print(f'The number {value} is classified as {result}.')