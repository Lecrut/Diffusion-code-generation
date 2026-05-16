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
        if factor == 0:
            results[other_unit] = float('inf') if distance != 0 else 0
        else:
            results[other_unit] = distance * factor
    return results
if __name__ == '__main__':
    distance_value = 10
    unit_value = 'km'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"Distance: {distance_value} {unit_value}")
        print("Conversions:")
        for unit, value in converted_distances.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)
    print("\n--- Sample 2 (Metric) ---")
    distance_value_2 = 500
    unit_value_2 = 'm'
    try:
        converted_distances_2 = convert_distance(distance_value_2, unit_value_2)
        print(f"Distance: {distance_value_2} {unit_value_2}")
        print("Conversions:")
        for unit, value in converted_distances_2.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)
    print("\n--- Sample 3 (Unsupported Unit) ---")
    distance_value_3 = 100
    unit_value_3 = 'lightyear'
    try:
        converted_distances_3 = convert_distance(distance_value_3, unit_value_3)
        print(f"Distance: {distance_value_3} {unit_value_3}")
        print("Conversions:")
        for unit, value in converted_distances_3.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)