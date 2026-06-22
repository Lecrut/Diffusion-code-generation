def analyze_lengths(len1, len2):
    min_len = min(len1, len2)
    max_len = max(len1, len2)
    abs_diff = abs(len1 - len2)
    return (min_len, max_len, abs_diff)

if __name__ == '__main__':
    result = analyze_lengths(10, 20)
    print(result)