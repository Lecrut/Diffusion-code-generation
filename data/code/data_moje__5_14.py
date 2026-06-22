def compare_lengths(length1_value, length1_unit, length2_value, length2_unit):
    def to_inches(value, unit):
        unit_lower = unit.lower()
        if unit_lower == 'inches' or unit_lower == 'in':
            return value
        elif unit_lower == 'cm' or unit_lower == 'centimeters':
            return value / 2.54
        elif unit_lower == 'm' or unit_lower == 'meters':
            return value * 39.3701
        elif unit_lower == 'ft' or unit_lower == 'feet':
            return value * 12
        else:
            raise ValueError(f"Unsupported unit: {unit}")

    inches1 = to_inches(length1_value, length1_unit)
    inches2 = to_inches(length2_value, length2_unit)

    if abs(inches1 - inches2) < 1e-9:
        return 0
    elif inches1 > inches2:
        return 1
    else:
        return -1

if __name__ == '__main__':
    result = compare_lengths(12, 'inches', 30.48, 'cm')
    print(result)