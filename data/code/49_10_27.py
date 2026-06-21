def calculate_lengths(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Lengths must be positive numbers")
    
    difference = abs(a - b)
    larger = max(a, b)
    smaller = min(a, b)
    ratio = larger / smaller
    
    return {
        'original_lengths': (a, b),
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    length1 = 20
    length2 = 8
    result = calculate_lengths(length1, length2)
    print(result)