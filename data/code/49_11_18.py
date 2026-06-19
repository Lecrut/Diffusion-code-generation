def analyze_lengths(len1, len2):
    if len1 <= 0 or len2 <= 0:
        return {'error': 'Lengths must be positive numbers'}
    
    smaller = min(len1, len2)
    larger = max(len1, len2)
    
    result = {
        'length1': len1,
        'length2': len2,
        'difference': larger - smaller,
        'ratio': larger / smaller
    }
    
    return result

if __name__ == '__main__':
    sample_length1 = 7
    sample_length2 = 14
    result = analyze_lengths(sample_length1, sample_length2)
    print(result)