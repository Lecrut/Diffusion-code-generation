def compare_measurements(length_a, length_b):
    difference = length_a - length_b
    ratio = length_a / length_b
    is_greater = length_a > length_b
    return difference, ratio, is_greater

if __name__ == '__main__':
    sample_a = 10.5
    sample_b = 8.3
    result = compare_measurements(sample_a, sample_b)
    print(result)