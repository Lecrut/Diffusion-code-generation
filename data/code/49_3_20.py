def analyze_lengths(len1, len2):
    MIN_VALUE = min(len1, len2)
    MAX_VALUE = max(len1, len2)
    DIFFERENCE = abs(len1 - len2)
    return (MIN_VALUE, MAX_VALUE, DIFFERENCE)

if __name__ == '__main__':
    length_a = 45.6
    length_b = 98.7
    result = analyze_lengths(length_a, length_b)
    print(result)