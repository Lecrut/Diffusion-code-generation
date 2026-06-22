def compare_measurements(length_a, length_b):
    difference = length_a - length_b
    if length_b != 0:
        ratio = length_a / length_b
    else:
        ratio = float('inf') if length_a > 0 else (float('-inf') if length_a < 0 else 0)
    is_greater = length_a > length_b
    return difference, ratio, is_greater

if __name__ == '__main__':
    length1 = 10.5
    length2 = 7.2
    diff, rat, greater = compare_measurements(length1, length2)
    print(diff, rat, greater)