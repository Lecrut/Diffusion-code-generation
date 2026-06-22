def calculate_lengths(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
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
    length1 = 7.5
    length2 = 3.0
    try:
        result = calculate_lengths(length1, length2)
        print(result)
    except Exception as e:
        print(f"Error: {e}")