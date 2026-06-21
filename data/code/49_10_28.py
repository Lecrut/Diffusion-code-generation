def calculate_lengths(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Lengths must be positive numbers")
    
    smaller_length = min(a, b)
    larger_length = max(a, b)
    
    difference = abs(a - b)
    ratio = larger_length / smaller_length
    
    return {
        'original_lengths': (a, b),
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    length1 = 8
    length2 = 3
    result = calculate_lengths(length1, length2)
    print(result)