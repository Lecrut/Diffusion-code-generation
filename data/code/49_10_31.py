def validate_lengths(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both lengths must be numbers")
    if a <= 0 or b <= 0:
        raise ValueError("Lengths must be positive numbers")

def calculate_lengths(a, b):
    validate_lengths(a, b)
    difference = abs(a - b)
    ratio = max(a, b) / min(a, b)
    return {
        'original_lengths': (a, b),
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    length1 = 7.5
    length2 = 3.0
    result = calculate_lengths(length1, length2)
    print(result)