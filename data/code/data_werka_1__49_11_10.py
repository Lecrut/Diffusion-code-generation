def compare_lengths(len1, len2):
    if len1 == len2:
        return {'length1': len1, 'length2': len2, 'difference': 0, 'ratio': 1}
    
    smaller = min(len1, len2)
    larger = max(len1, len2)
    
    return {
        'length1': len1,
        'length2': len2,
        'difference': larger - smaller,
        'ratio': larger / smaller
    }

if __name__ == '__main__':
    a = 7
    b = 21
    result = compare_lengths(a, b)
    print(result)