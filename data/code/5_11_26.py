def compare_measurements(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2 if length2 != 0 else float('inf')
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    measurement1 = 15.5
    measurement2 = 10.0
    result = compare_measurements(measurement1, measurement2)
    print(result)