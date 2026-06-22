def calculate_lengths(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Lengths must be positive numbers")
    
    original_lengths = (a, b)
    difference = abs(a - b)
    larger_length = max(a, b)
    smaller_length = min(a, b)
    ratio = larger_length / smaller_length
    
    return {
        'original_lengths': original_lengths,
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    length_a = 15
    length_b = 9
    result = calculate_lengths(length_a, length_b)
    print(result)