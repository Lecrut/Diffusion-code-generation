import math
def convert_distance(distance, target_unit):
    if target_unit == 0:
        raise ValueError("Target unit cannot be zero.")
    if target_unit == 1:
        return distance
    if target_unit == 1000:
        return distance / 1000.0
    if target_unit == 1000000:
        return distance / 1000000.0
    if target_unit == 1000000000:
        return distance / 1000000000.0
    if target_unit == 1:
        return distance
    if target_unit == 100:
        return distance / 100.0
    if target_unit == 10:
        return distance / 10.0
    if target_unit == 0.0:
        raise ValueError("Target unit cannot be zero.")
    try:
        conversion_factor = 1.0
        if target_unit != 1:
            conversion_map = {
                'm': 1.0,
                'km': 1000.0,
                'cm': 0.01,
                'mm': 0.001,
                'mi': 1609.344,
                'ft': 3.28084,
                'in': 2.54,
            }
            if target_unit in conversion_map:
                factor = conversion_map[target_unit]
                return distance * factor
            else:
                raise ValueError(f"Unsupported target unit: {target_unit}")
        else:
            return distance
    except ValueError as e:
        raise e
    except Exception as e:
        raise ValueError(f"An unexpected error occurred during conversion: {e}")
if __name__ == '__main__':
    distance_m = 1000.0
    target_km = 1.0
    target_cm = 50.0
    target_mi = 1.0
    target_unknown = 5.0
    print(f"Distance: {distance_m} meters")
    try:
        result_km = convert_distance(distance_m, 'km')
        print(f"Converted to km: {result_km}")
        result_cm = convert_distance(distance_m, 'cm')
        print(f"Converted to cm: {result_cm}")
        result_mi = convert_distance(distance_m, 'mi')
        print(f"Converted to mi: {result_mi}")
        result_self = convert_distance(distance_m, 'm')
        print(f"Converted to m: {result_self}")
        print("\nTesting division by zero handling:")
        try:
            convert_distance(10.0, 0.0)
        except ValueError as e:
            print(f"Caught expected error for target unit 0.0: {e}")
        print("\nTesting unsupported unit handling:")
        try:
            convert_distance(10.0, 'lightyear')
        except ValueError as e:
            print(f"Caught expected error for unsupported unit: {e}")
    except ValueError as e:
        print(f"A critical error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")