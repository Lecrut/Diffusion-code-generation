import math
def convert_distance(distance, unit):
    conversions = {
        'm': 1,
        'km': 1000,
        'mi': 1609.34,
        'cm': 0.01,
        'mm': 0.001,
        'in': 39.3701,
        'ft': 3.28084,
        'yd': 1.09361,
        'mile': 1609.34,
        'kilometer': 1000,
        'meter': 1,
        'centimeter': 100,
        'millimeter': 10,
        'inch': 2.54,
        'foot': 12,
        'yard': 3,
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    if distance == 0:
        return {u: 0 for u in conversions.keys()}
    base_value = distance
    results = {}
    for target_unit, factor in conversions.items():
        if target_unit == unit:
            results[target_unit] = distance
            continue
        if unit == 'm':
            results[target_unit] = distance * factor
        elif unit == 'km':
            results[target_unit] = distance * factor
        elif unit == 'mi':
            results[target_unit] = distance * factor
        elif unit == 'cm':
            results[target_unit] = distance * factor
        elif unit == 'mm':
            results[target_unit] = distance * factor
        elif unit == 'in':
            results[target_unit] = distance * factor
        elif unit == 'ft':
            results[target_unit] = distance * factor
        elif unit == 'yd':
            results[target_unit] = distance * factor
        elif unit == 'mile':
            results[target_unit] = distance * factor
        elif unit == 'kilometer':
            results[target_unit] = distance * factor
        elif unit == 'meter':
            results[target_unit] = distance * factor
        elif unit == 'centimeter':
            results[target_unit] = distance * factor
        elif unit == 'millimeter':
            results[target_unit] = distance * factor
        elif unit == 'inch':
            results[target_unit] = distance * factor
        elif unit == 'foot':
            results[target_unit] = distance * factor
        elif unit == 'yard':
            results[target_unit] = distance * factor
    return results
if __name__ == '__main__':
    distance_value = 10
    unit_value = 'km'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"Original Distance: {distance_value} {unit_value}")
        print("Converted Distances:")
        for unit, value in converted_distances.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)
    distance_value = 1000
    unit_value = 'm'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"\nOriginal Distance: {distance_value} {unit_value}")
        print("Converted Distances:")
        for unit, value in converted_distances.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)
    distance_value = 1
    unit_value = 'mi'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"\nOriginal Distance: {distance_value} {unit_value}")
        print("Converted Distances:")
        for unit, value in converted_distances.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)