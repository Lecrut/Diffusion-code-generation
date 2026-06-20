def compare_measurements(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    val1 = 10.5
    val2 = 7.2
    diff, r, greater = compare_measurements(val1, val2)
    print(diff)
    print(r)
    print(greater)