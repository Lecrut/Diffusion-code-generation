def validate_lengths(len1, len2):
    if not (isinstance(len1, (int, float)) and isinstance(len2, (int, float))):
        raise ValueError("Both lengths must be numbers.")
    if len1 <= 0 or len2 <= 0:
        raise ValueError("Both lengths must be positive.")

def compare_lengths(len1, len2):
    validate_lengths(len1, len2)
    return {
        'length1': len1,
        'length2': len2,
        'difference': abs(len1 - len2),
        'ratio': max(len1, len2) / min(len1, len2)
    }

if __name__ == '__main__':
    sample_length1 = 7
    sample_length2 = 21
    result = compare_lengths(sample_length1, sample_length2)
    print(result)