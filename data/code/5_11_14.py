def compare_measurements(length1, length2):
    difference = length1 - length2
    if length2 != 0:
        ratio = length1 / length2
    else:
        ratio = 0
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    len1 = 15.5
    len2 = 10.0
    diff, rat, greater = compare_measurements(len1, len2)
    print(diff)
    print(rat)
    print(greater)