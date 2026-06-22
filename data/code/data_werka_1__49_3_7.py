def analyze_lengths(len1, len2):
    min_len = min(len1, len2)
    max_len = max(len1, len2)
    diff = abs(len1 - len2)
    return (min_len, max_len, diff)

if __name__ == '__main__':
    length1 = 30.5
    length2 = 18.4
    result = analyze_lengths(length1, length2)
    print(result)