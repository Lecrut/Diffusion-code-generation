def calculate_lengths(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Lengths must be positive numbers")
    difference = abs(a - b)
    ratio = max(a, b) / min(a, b)
    return {
        'lengths': (a, b),
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    sample_lengths = {'length1': 15, 'length2': 3}
    result = calculate_lengths(sample_lengths['length1'], sample_lengths['length2'])
    print(result)