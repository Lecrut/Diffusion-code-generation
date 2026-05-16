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
        return {unit: 0 for other_unit in conversions if other_unit != unit}
    results = {}
    for other_unit, factor in conversions.items():
        if other_unit == unit:
            continue
        if other_unit == 'mile':
            results[other_unit] = distance / conversions[unit] * conversions['mi']
        else:
            results[other_unit] = distance * factor
    return results
if __name__ == '__main__':
    distance_value = 10
    unit_value = 'km'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"Original: {distance_value} {unit_value}")
        print("Conversions:")
        for unit, result in converted_distances.items():
            print(f"{unit}: {result:.4f}")
    except ValueError as e:
        print(e)
    distance_value = 1000
    unit_value = 'm'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"\nOriginal: {distance_value} {unit_value}")
        print("Conversions:")
        for unit, result in converted_distances.items():
            print(f"{unit}: {result:.4f}")
    except ValueError as e:
        print(e)
    distance_value = 1
    unit_value = 'mi'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"\nOriginal: {distance_value} {unit_value}")
        print("Conversions:")
        for unit, result in converted_distances.items():
            print(f"{unit}: {result:.4f}")
    except ValueError as e:
        print(e)