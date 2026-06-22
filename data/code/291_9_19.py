def compare_lengths(length1, unit1, length2, unit2):
    conversion_factors = {'rod': 5.0292, 'meter': 1}
    if unit1 not in conversion_factors or unit2 not in conversion_factors:
        raise ValueError('Invalid unit of measurement')
    length1_converted = length1 * conversion_factors[unit1]
    length2_converted = length2 * conversion_factors[unit2]
    if length1_converted == length2_converted:
        return 'Equal'
    elif length1_converted < length2_converted:
        return f'{length1} {unit1} is shorter than {length2} {unit2}'
    else:
        return f'{length1} {unit1} is longer than {length2} {unit2}'
if __name__ == '__main__':
    print(compare_lengths(10, 'rod', 50.292, 'meter'))
    print(compare_lengths(5, 'rod', 25, 'meter'))
    print(compare_lengths(20, 'rod', 100, 'meter'))