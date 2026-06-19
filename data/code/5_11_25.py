def compare_measurements(length1, length2):
    difference = abs(length1 - length2)
    ratio = length1 / length2 if length2 != 0 else float('inf')
    is_first_greater = length1 > length2
    return difference, ratio, is_first_greater

if __name__ == '__main__':
    length_a = 15.5
    length_b = 9.3
    result = compare_measurements(length_a, length_b)
    print(result)