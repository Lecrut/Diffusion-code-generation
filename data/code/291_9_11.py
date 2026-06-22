CONVERSION_FACTOR = {'rod': 5.0292, 'meter': 1}

def compare_lengths(length1, unit1, length2, unit2):
    length1_converted = length1 * CONVERSION_FACTOR[unit1]
    length2_converted = length2 * CONVERSION_FACTOR[unit2]
    if length1_converted == length2_converted:
        return 'Equal'
    elif length1_converted > length2_converted:
        return f'{length1} {unit1} is longer than {length2} {unit2}'
    else:
        return f'{length2} {unit2} is longer than {length1} {unit1}'

if __name__ == '__main__':
    print(compare_lengths(1, 'rod', 5.0292, 'meter'))
    print(compare_lengths(1, 'rod', 3, 'rods'))
    print(compare_lengths(2, 'rods', 10, 'meters'))