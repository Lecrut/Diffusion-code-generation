def compare_measurements(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2 if length2 != 0 else float('inf')
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    length1 = 15.5
    length2 = 9.3
    difference, ratio, is_greater = compare_measurements(length1, length2)
    print(difference)
    print(ratio)
    print(is_greater)