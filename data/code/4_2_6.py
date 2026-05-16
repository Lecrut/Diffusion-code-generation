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
        return {unit: 0 for other_unit in conversions.keys() if other_unit != unit}
    result = {}
    for target_unit, factor in conversions.items():
        if target_unit == unit:
            continue
        if target_unit == 'mile':
            if unit in ['m', 'km', 'cm', 'mm', 'in', 'ft', 'yd']:
                value = distance * (1609.34 / 1000) if unit == 'km' else distance * (1609.34 / 1000000) if unit == 'm' else distance * (1609.34 / 100000000)
                if unit == 'm':
                    value = distance * 1609.34 / 1000
                elif unit == 'km':
                    value = distance * 1609.34
                elif unit == 'cm':
                    value = distance * 160934 / 1000000
                elif unit == 'mm':
                    value = distance * 160934 / 100000000
                elif unit == 'in':
                    value = distance * 1609.34 / 2.54
                elif unit == 'ft':
                    value = distance * 3.28084 / 0.3048
                elif unit == 'yd':
                    value = distance * 3.28084 / 0.9144
                else:
                    value = distance * factor
            else:
                value = distance * factor
        else:
            value = distance * factor
        result[target_unit] = value
    return result
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
    print("\n--- Test Case 2 (Metric) ---")
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
    print("\n--- Test Case 3 (Imperial) ---")
    distance_value_3 = 1
    unit_value_3 = 'mi'
    try:
        converted_distances_3 = convert_distance(distance_value_3, unit_value_3)
        print(f"Distance: {distance_value_3} {unit_value_3}")
        print("Conversions:")
        for unit, value in converted_distances_3.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(e)