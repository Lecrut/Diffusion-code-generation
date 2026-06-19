def analyze_lengths(len1, len2):
    min_len = min(len1, len2)
    max_len = max(len1, len2)
    abs_diff = abs(len1 - len2)
    return (min_len, max_len, abs_diff)

if __name__ == '__main__':
    length1 = 10.5
    length2 = 4.8
    result = analyze_lengths(length1, length2)
    print(result)