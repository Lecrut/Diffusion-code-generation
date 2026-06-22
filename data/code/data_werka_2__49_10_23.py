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
    result = calculate_lengths(10, 5)
    print(result)