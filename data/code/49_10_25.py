def calculate_lengths(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Lengths must be positive numbers")
    
    difference = abs(a - b)
    ratio = max(a, b) / min(a, b)
    
    return {
        'length1': a,
        'length2': b,
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    length1 = 10
    length2 = 5
    result = calculate_lengths(length1, length2)
    print(result)