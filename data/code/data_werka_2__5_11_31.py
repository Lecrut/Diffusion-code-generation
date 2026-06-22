def calculate_difference(length1, length2):
    return length1 - length2

def calculate_ratio(length1, length2):
    if length2 == 0:
        return float('inf')
    return length1 / length2

def is_first_greater(length1, length2):
    return length1 > length2

def compare_measurements(length1, length2):
    difference = calculate_difference(length1, length2)
    ratio = calculate_ratio(length1, length2)
    is_greater = is_first_greater(length1, length2)
    return difference, ratio, is_greater

if __name__ == '__main__':
    length1 = 20.7
    length2 = 8.4
    result = compare_measurements(length1, length2)
    print(result)