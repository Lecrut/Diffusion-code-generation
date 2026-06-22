def analyze_lengths(length1, length2):
    smaller = min(length1, length2)
    larger = max(length1, length2)
    difference = larger - smaller
    ratio = larger / smaller if smaller != 0 else float('inf')
    
    return {
        'original_length1': length1,
        'original_length2': length2,
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    sample_length1 = 7
    sample_length2 = 14
    result = analyze_lengths(sample_length1, sample_length2)
    print(result)