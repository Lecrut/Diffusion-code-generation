def compare_rods_and_meters(length1, unit1, length2, unit2):
    conversion_factor = 5.0292
    if unit1 not in ['rods', 'meters'] or unit2 not in ['rods', 'meters']:
        raise ValueError("Invalid units. Only 'rods' and 'meters' are allowed.")
    length1_converted = length1 * conversion_factor if unit1 == 'rods' else length1
    length2_converted = length2 * conversion_factor if unit2 == 'rods' else length2
    if length1_converted < length2_converted:
        return -1
    elif length1_converted > length2_converted:
        return 1
    else:
        return 0
if __name__ == '__main__':
    print(compare_rods_and_meters(1, 'rods', 5.0292, 'meters'))
    print(compare_rods_and_meters(1, 'rods', 3, 'rods'))
    print(compare_rods_and_meters(2, 'rods', 10, 'meters'))