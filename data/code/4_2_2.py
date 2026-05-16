import math
def convert_distance(distance, unit):
    conversions = {
        'm': 1,
        'km': 1000,
        'mi': 1609.34,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mile': 1609.34,
        'kilometer': 1000,
        'meter': 1,
        'centimeter': 100,
        'millimeter': 10,
        'inch': 2.54,
        'foot': 3.28084,
        'yard': 3.0825,
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    if distance == 0:
        return {u: 0 for u in conversions}
    results = {}
    for target_unit, factor in conversions.items():
        if target_unit == unit:
            results[target_unit] = distance
            continue
        if unit == 'm':
            value = distance * factor
        elif unit == 'km':
            value = distance * factor
        elif unit == 'mi':
            value = distance * factor
        elif unit == 'cm':
            value = distance * factor
        elif unit == 'mm':
            value = distance * factor
        elif unit == 'in':
            value = distance * factor
        elif unit == 'ft':
            value = distance * factor
        elif unit == 'yd':
            value = distance * factor
        elif unit == 'mile':
            value = distance * factor
        elif unit == 'kilometer':
            value = distance * factor
        elif unit == 'meter':
            value = distance * factor
        elif unit == 'centimeter':
            value = distance * factor
        elif unit == 'millimeter':
            value = distance * factor
        elif unit == 'inch':
            value = distance * factor
        elif unit == 'foot':
            value = distance * factor
        elif unit == 'yard':
            value = distance * factor
        else:
            continue
        results[target_unit] = value
    return results
if __name__ == '__main__':
    test_distance = 10
    test_unit = 'km'
    print(f"Converting {test_distance} {test_unit} to all supported units:")
    try:
        converted_distances = convert_distance(test_distance, test_unit)
        for unit, value in converted_distances.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)
    print("\n--- Another Test ---")
    test_distance_2 = 500
    test_unit_2 = 'm'
    print(f"Converting {test_distance_2} {test_unit_2} to all supported units:")
    try:
        converted_distances_2 = convert_distance(test_distance_2, test_unit_2)
        for unit, value in converted_distances_2.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)
    print("\n--- Test Unsupported Unit ---")
    try:
        convert_distance(10, 'lightyear')
    except ValueError as e:
        print(e)