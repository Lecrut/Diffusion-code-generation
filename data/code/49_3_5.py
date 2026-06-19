def analyze_lengths(len1, len2):
    minimum = min(len1, len2)
    maximum = max(len1, len2)
    difference = abs(len1 - len2)
    return (minimum, maximum, difference)

if __name__ == '__main__':
    result = analyze_lengths(10, 20)
    print(result)