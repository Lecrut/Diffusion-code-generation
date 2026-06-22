def analyze_lengths(len1, len2):
    MIN_LEN = min(len1, len2)
    MAX_LEN = max(len1, len2)
    DIFFERENCE = abs(len1 - len2)
    return (MIN_LEN, MAX_LEN, DIFFERENCE)

if __name__ == '__main__':
    length1 = 30.5
    length2 = 45.2
    result = analyze_lengths(length1, length2)
    print(result)