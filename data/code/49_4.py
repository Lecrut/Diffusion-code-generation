def analyze_lengths(len1, len2):
    minimum = min(len1, len2)
    maximum = max(len1, len2)
    difference = abs(len1 - len2)
    return (minimum, maximum, difference)
if __name__ == '__main__':
    a = 10
    b = 25
    result = analyze_lengths(a, b)
    print(result)