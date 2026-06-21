def compare_measurements(length1, length2):
    difference = length1 - length2
    ratio = float('inf') if length2 == 0 else length1 / length2
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    length1 = 20.75
    length2 = 12.5
    result = compare_measurements(length1, length2)
    print(result)