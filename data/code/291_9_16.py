def compare_lengths(length1, unit1, length2, unit2):
    conversion_factor = {'rod': 5.0292, 'meter': 1}
    if unit1 == unit2:
        return length1 == length2
    converted_length1 = length1 * conversion_factor[unit1]
    converted_length2 = length2 * conversion_factor[unit2]
    return converted_length1 == converted_length2
if __name__ == '__main__':
    print(compare_lengths(10, 'rod', 5.0292, 'meter'))
    print(compare_lengths(10, 'rod', 5.03, 'meter'))
    print(compare_lengths(10, 'meter', 10, 'rod'))
    print(compare_lengths(10, 'meter', 10, 'meter'))