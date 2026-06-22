def compare_lengths(length1, unit1, length2, unit2):
    conversion_factor = {'rod': 5.0292, 'meter': 1}
    length1_converted = length1 * conversion_factor[unit1]
    length2_converted = length2 * conversion_factor[unit2]
    if length1_converted == length2_converted:
        return 'Equal'
    elif length1_converted > length2_converted:
        return 'First longer'
    else:
        return 'Second longer'
if __name__ == '__main__':
    print(compare_lengths(10, 'rod', 50.292, 'meter'))
    print(compare_lengths(5, 'rod', 25, 'meter'))
    print(compare_lengths(3, 'rod', 15, 'meter'))