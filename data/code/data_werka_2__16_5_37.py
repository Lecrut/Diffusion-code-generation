def determine_positivity(num):
    POSITIVE_THRESHOLD = 0
    NEGATIVE_THRESHOLD = 0
    if num > POSITIVE_THRESHOLD:
        return 'Positive'
    elif num < NEGATIVE_THRESHOLD:
        return 'Negative'
    else:
        return 'Zero'
assert determine_positivity(10) == 'Positive', 'Test case for positive number failed'
assert determine_positivity(-5) == 'Negative', 'Test case for negative number failed'
assert determine_positivity(0) == 'Zero', 'Test case for zero failed'
if __name__ == '__main__':
    sample_values = [10, -5, 0]
    results = {value: determine_positivity(value) for value in sample_values}
    for value, result in results.items():
        print(f'The number {value} is {result}.')