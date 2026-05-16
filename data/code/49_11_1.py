def compare_lengths(len1, len2):
    return (min(len1, len2), max(len1, len2))
if __name__ == '__main__':
    a = 15
    b = 28
    result = compare_lengths(a, b)
    print(result)