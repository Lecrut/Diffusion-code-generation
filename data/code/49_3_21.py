def analyze_lengths(len1, len2):
    min_length = min(len1, len2)
    max_length = max(len1, len2)
    absolute_difference = abs(len1 - len2)
    return (min_length, max_length, absolute_difference)

if __name__ == '__main__':
    length_a = 45.7
    length_b = 63.2
    result = analyze_lengths(length_a, length_b)
    print(result)