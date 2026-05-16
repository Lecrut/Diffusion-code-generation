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
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    if distance == 0:
        return {unit: 0 for other_unit in conversions.keys() if other_unit != unit}
    results = {}
    for other_unit, factor in conversions.items():
        if other_unit == unit:
            continue
        if factor == 0:
            results[other_unit] = float('inf') if distance != 0 else 0
            continue
        if unit == 'm':
            value = distance * factor
        elif unit == 'km':
            value = distance / factor
        elif unit == 'mi':
            value = distance / factor
        else:
            value = distance * factor
        results[other_unit] = value
    return results
if __name__ == '__main__':
    distance_value = 10
    unit_value = 'km'
    converted_distances = convert_distance(distance_value, unit_value)
    print(f"Original Distance: {distance_value} {unit_value}")
    print("Converted Distances:")
    for unit, value in converted_distances.items():
        print(f"{unit}: {value:.4f}")