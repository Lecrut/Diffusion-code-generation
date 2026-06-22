def convert_to_meters(length, unit):
    conversion_factor = {'rod': 5.0292, 'meter': 1}
    return length * conversion_factor.get(unit, 0)

def compare_lengths(length1, unit1, length2, unit2):
    length1_m = convert_to_meters(length1, unit1)
    length2_m = convert_to_meters(length2, unit2)
    
    if length1_m == length2_m:
        return 0
    elif length1_m > length2_m:
        return 1
    else:
        return -1

if __name__ == '__main__':
    print(compare_lengths(1, 'rods', 5.0292, 'meters'))
    print(compare_lengths(1, 'rods', 3, 'rods'))
    print(compare_lengths(2, 'rods', 10, 'meters'))