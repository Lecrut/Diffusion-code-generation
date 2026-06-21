def calculate_lengths(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Lengths must be positive numbers")
    
    def compute_difference(x, y):
        return abs(x - y)
    
    def compute_ratio(x, y):
        return max(x, y) / min(x, y)
    
    difference = compute_difference(a, b)
    ratio = compute_ratio(a, b)
    
    return {
        'original_lengths': (a, b),
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    length1 = 15
    length2 = 3
    result = calculate_lengths(length1, length2)
    print(result)