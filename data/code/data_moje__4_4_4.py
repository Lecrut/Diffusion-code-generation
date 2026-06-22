def convert_distance(distance, target_unit):
    units = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.344,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }
    if target_unit not in units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    if units[target_unit] == 0:
        raise ZeroDivisionError("Conversion factor is zero")
    converted = distance / units[target_unit]
    return converted

if __name__ == '__main__':
    result1 = convert_distance(1000, 'kilometer')
    print(result1)
    result2 = convert_distance(1, 'mile')
    print(result2)
    result3 = convert_distance(5, 'foot')
    print(result3)