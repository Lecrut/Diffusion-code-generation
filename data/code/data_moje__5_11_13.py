def compare_lengths(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    a = 10.5
    b = 5.2
    diff, ratio, greater = compare_lengths(a, b)
    print(diff)
    print(ratio)
    print(greater)