import math
def convert_distance(distance, unit):
    conversions = {
        'm': 1,
        'km': 1000,
        'mi': 1609.34,
        'ft': 0.3048,
        'in': 0.0254
    }
    if unit not in conversions:
        raise ValueError("Unsupported unit")
    results = {}
    for other_unit, factor in conversions.items():
        if other_unit != unit:
            if factor == 0:
                results[other_unit] = 0
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
        print(f"Error: {e}")
    distance_value = 1000
    unit_value = 'm'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"\nDistance: {distance_value} {unit_value}")
        print("Conversions:")
        for unit, value in converted_distances.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 1
    unit_value = 'mi'
    try:
        converted_distances = convert_distance(distance_value, unit_value)
        print(f"\nDistance: {distance_value} {unit_value}")
        print("Conversions:")
        for unit, value in converted_distances.items():
            print(f"{unit}: {value:.4f}")
    except ValueError as e:
        print(f"Error: {e}")