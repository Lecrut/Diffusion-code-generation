def analyze_lengths(len1, len2):
    min_length = min(len1, len2)
    max_length = max(len1, len2)
    difference = abs(len1 - len2)
    return (min_length, max_length, difference)

if __name__ == '__main__':
    length1 = 30.5
    length2 = 20.8
    result = analyze_lengths(length1, length2)
    print(result)