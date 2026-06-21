def analyze_lengths(len1, len2):
    if not isinstance(len1, (int, float)) or not isinstance(len2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    min_len = len1 if len1 < len2 else len2
    max_len = len1 if len1 > len2 else len2
    abs_diff = abs(len1 - len2)
    
    return (min_len, max_len, abs_diff)

if __name__ == '__main__':
    length1 = 45.3
    length2 = 67.8
    result = analyze_lengths(length1, length2)
    print(result)