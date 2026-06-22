def compare_measurements(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2 if length2 != 0 else float('inf')
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    LENGTH1 = 20.75
    LENGTH2 = 8.25
    result_difference, result_ratio, result_is_greater = compare_measurements(LENGTH1, LENGTH2)
    print(f"Difference: {result_difference}")
    print(f"Ratio: {result_ratio}")
    print(f"Is First Greater: {result_is_greater}")