def calculate_lengths(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Lengths must be positive numbers")
    
    difference = abs(a - b)
    ratio = max(a, b) / min(a, b)
    
    return {
        'original_lengths': (a, b),
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    LENGTH1 = 20
    LENGTH2 = 8
    result = calculate_lengths(LENGTH1, LENGTH2)
    print(result)