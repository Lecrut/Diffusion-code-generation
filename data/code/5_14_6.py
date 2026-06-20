def compare_lengths(length_a, unit_a, length_b, unit_b):
    unit_a = unit_a.lower()
    unit_b = unit_b.lower()
    conversion_to_cm = {
        'cm': 1.0,
        'centimeter': 1.0,
        'centimeters': 1.0,
        'inch': 2.54,
        'inches': 2.54,
        'in': 2.54
    }
    factor_a = conversion_to_cm.get(unit_a)
    factor_b = conversion_to_cm.get(unit_b)
    if factor_a is None or factor_b is None:
        raise ValueError("Unsupported unit")
    cm_a = length_a * factor_a
    cm_b = length_b * factor_b
    if cm_a > cm_b:
        return "A is longer"
    elif cm_b > cm_a:
        return "B is longer"
    else:
        return "Equal length"

if __name__ == '__main__':
    result = compare_lengths(10, 'inches', 25.4, 'cm')
    print(result)