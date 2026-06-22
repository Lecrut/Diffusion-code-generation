def compare_lengths(length1, unit1, length2, unit2):
    conversion = {'rod': 5.0292, 'meter': 1}
    length1_converted = length1 * conversion[unit1]
    length2_converted = length2 * conversion[unit2]
    if length1_converted == length2_converted:
        return 'Equal'
    elif length1_converted > length2_converted:
        return 'First longer'
    else:
        return 'Second longer'
if __name__ == '__main__':
    print(compare_lengths(10, 'rod', 50.292, 'meter'))
    print(compare_lengths(5, 'rod', 10, 'meter'))
    print(compare_lengths(10, 'meter', 5, 'rod'))