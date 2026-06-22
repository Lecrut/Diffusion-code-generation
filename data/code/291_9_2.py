def compare_lengths(length1, unit1, length2, unit2):
    conversion_factor = 5.0292
    if unit1 == 'meters':
        length1 *= conversion_factor
    if unit2 == 'meters':
        length2 *= conversion_factor
    if length1 < length2:
        return -1
    elif length1 > length2:
        return 1
    else:
        return 0
if __name__ == '__main__':
    print(compare_lengths(1, 'rods', 5.0292, 'meters'))
    print(compare_lengths(1, 'rods', 3, 'rods'))
    print(compare_lengths(2, 'rods', 10, 'meters'))