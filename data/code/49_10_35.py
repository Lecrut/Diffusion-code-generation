def calculate_lengths(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Lengths must be positive numbers")
    
    difference = abs(length1 - length2)
    ratio = max(length1, length2) / min(length1, length2)
    
    return {
        'length1': length1,
        'length2': length2,
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    sample_length1 = 10.0
    sample_length2 = 5.0
    result = calculate_lengths(sample_length1, sample_length2)
    print(result)