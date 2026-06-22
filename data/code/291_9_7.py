def compare_lengths(length1, unit1, length2, unit2):
    conversion_factors = {'rod': 5.0292, 'meter': 1}
    if unit1 == unit2:
        return length1 == length2
    converted_length1 = length1 * conversion_factors[unit1]
    converted_length2 = length2 * conversion_factors[unit2]
    return converted_length1 == converted_length2
if __name__ == '__main__':
    print(compare_lengths(5, 'rod', 25.146, 'meter'))
    print(compare_lengths(3, 'rod', 10, 'meter'))
    print(compare_lengths(7, 'meter', 7, 'rod'))