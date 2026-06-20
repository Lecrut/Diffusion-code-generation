def compare_lengths(length1_value, length1_unit, length2_value, length2_unit):

    def to_cm(value, unit):
        if unit.lower() == 'inches' or unit.lower() == 'in':
            return value * 2.54
        elif unit.lower() == 'cm' or unit.lower() == 'centimeters':
            return value
        else:
            raise ValueError(f'Unsupported unit: {unit}')
    norm1 = to_cm(length1_value, length1_unit)
    norm2 = to_cm(length2_value, length2_unit)
    if norm1 < norm2:
        comp = '<'
    elif norm1 > norm2:
        comp = '>'
    else:
        comp = '='
    return (norm1, norm2, comp)
if __name__ == '__main__':
    val1, unit1 = (10, 'inches')
    val2, unit2 = (25, 'cm')
    norm1, norm2, result = compare_lengths(val1, unit1, val2, unit2)
    print(norm1, norm2, result)