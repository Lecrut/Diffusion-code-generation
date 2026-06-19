def analyze_lengths(len1, len2):
    min_length = min(len1, len2)
    max_length = max(len1, len2)
    difference = abs(len1 - len2)
    return (min_length, max_length, difference)

if __name__ == '__main__':
    result = analyze_lengths(10, 20)
    print(result)