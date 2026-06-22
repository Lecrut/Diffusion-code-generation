def compare_measurements(length1, length2):
    difference = abs(length1 - length2)
    ratio = length1 / length2 if length2 != 0 else float('inf')
    is_first_greater = length1 > length2
    return difference, ratio, is_first_greater

if __name__ == '__main__':
    length1 = 5.5
    length2 = 3.2
    result = compare_measurements(length1, length2)
    print(result)