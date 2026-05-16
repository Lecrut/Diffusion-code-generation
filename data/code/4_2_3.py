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
        'mi': 1609.34,
        'km': 1000,
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    if distance == 0:
        return {u: 0 for u in conversions.keys()}
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
        else:
            value = distance * factor
        results[target_unit] = value
    return results
if __name__ == '__main__':
    distance_value = 100
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