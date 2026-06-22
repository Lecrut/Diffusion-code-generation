def compare_measurements(length1, length2):
    difference = length1 - length2
    ratio = length1 / length2 if length2 != 0 else float('inf')
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    length1 = 15.5
    length2 = 10.0
    result = compare_measurements(length1, length2)
    print("Difference:", result[0])
    print("Ratio:", result[1])
    print("Is First Greater than Second:", result[2])