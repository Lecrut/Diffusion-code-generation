def compare_measurements(length1, length2):
    difference = length1 - length2
    if length2 == 0:
        ratio = None
    else:
        ratio = length1 / length2
    is_greater = length1 > length2
    return difference, ratio, is_greater

if __name__ == '__main__':
    sample_length1 = 10.5
    sample_length2 = 4.2
    result = compare_measurements(sample_length1, sample_length2)
    print(result)