def compare_measurements(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2 if length2 != 0 else float('inf')
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    LENGTH1 = 20.75
    LENGTH2 = 8.4
    result = compare_measurements(LENGTH1, LENGTH2)
    print(result)