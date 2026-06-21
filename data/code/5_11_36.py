def compare_measurements(length1, length2):
    difference = length1 - length2
    ratio = float('inf') if length2 == 0 else length1 / length2
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    LENGTH1 = 20.75
    LENGTH2 = 8.4
    result = compare_measurements(LENGTH1, LENGTH2)
    print(result)