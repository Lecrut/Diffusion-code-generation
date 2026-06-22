def analyze_lengths(len1, len2):
    min_length = min(len1, len2)
    max_length = max(len1, len2)
    difference = abs(len1 - len2)
    return (min_length, max_length, difference)

if __name__ == '__main__':
    length_a = 30.5
    length_b = 45.2
    result = analyze_lengths(length_a, length_b)
    print(result)