def compare_measurements(m1, m2):
    difference = m1 - m2
    ratio = m1 / m2
    is_greater = m1 > m2
    return difference, ratio, is_greater

if __name__ == '__main__':
    length_1 = 15.5
    length_2 = 10.0
    diff, rat, gt = compare_measurements(length_1, length_2)
    print(diff)
    print(rat)
    print(gt)