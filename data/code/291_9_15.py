ROD_TO_METER_CONVERSION = 5.0292

def compare_lengths(length1, unit1, length2, unit2):
    length1_converted = length1 * ROD_TO_METER_CONVERSION if unit1 == 'rods' else length1
    length2_converted = length2 * ROD_TO_METER_CONVERSION if unit2 == 'rods' else length2
    if length1_converted < length2_converted:
        return -1
    elif length1_converted > length2_converted:
        return 1
    else:
        return 0
if __name__ == '__main__':
    print(compare_lengths(1, 'rods', 5.0292, 'meters'))
    print(compare_lengths(1, 'rods', 3, 'rods'))
    print(compare_lengths(2, 'rods', 10, 'meters'))