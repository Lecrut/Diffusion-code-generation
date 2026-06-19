def compare_lengths(length1, length2):
    return (min(length1, length2), max(length1, length2))

if __name__ == '__main__':
    len1 = 15
    len2 = 10
    result = compare_lengths(len1, len2)
    print(result)