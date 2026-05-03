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
        'yard': 3.28084
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    if distance == 0:
        return {unit: 0 for other_unit in conversions if other_unit != unit}
    results = {}
    for target_unit, factor in conversions.items():
        if target_unit == unit:
            continue
        if target_unit == 'mile':
            if unit in ['m', 'km', 'cm', 'mm', 'in', 'ft', 'yd']:
                results[target_unit] = distance * factor
            else:
                results[target_unit] = distance * factor
        elif unit == 'mile':
            results[target_unit] = distance / factor
        else:
            results[target_unit] = distance * factor
    return results
if __name__ == '__main__':
    distance_value = 10
    unit_value = 'km'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"Original: {distance_value} {unit_value}")
        print("Conversions:")
        for unit, value in converted_distances.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)
    distance_value = 1000
    unit_value = 'm'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"\nOriginal: {distance_value} {unit_value}")
        print("Conversions:")
        for unit, value in converted_distances.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)
    distance_value = 1
    unit_value = 'mi'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"\nOriginal: {distance_value} {unit_value}")
        print("Conversions:")
        for unit, value in converted_distances.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)