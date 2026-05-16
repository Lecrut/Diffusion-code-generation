import math
def convert_distance(distance, target_unit):
    if target_unit == 0:
        raise ValueError("Target unit cannot be zero.")
    if target_unit == 1:
        return distance
    conversion_factors = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "mile": 1609.34,
        "foot": 3.28084,
        "inch": 39.3701,
    }
    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    base_unit = "meter"
    if target_unit == base_unit:
        return float(distance)
    factors = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "mile": 1 / 1609.34,                             
        "foot": 1 / 3.28084,                            
        "inch": 1 / 39.3701,                              
    }
    if target_unit not in factors:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    unit_to_meter = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "mile": 1609.34,
        "foot": 3.28084,
        "inch": 39.3701,
    }
    if target_unit not in unit_to_meter:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    factor = unit_to_meter[target_unit]
    if factor == 0:
        raise ZeroDivisionError("Conversion factor resulted in division by zero.")
    result = distance / factor
    return result
if __name__ == '__main__':
    distance_m = 1000.0
    target_km = convert_distance(distance_m, "kilometer")
    print(f"1000.0 meters to kilometers: {target_km}")
    distance_m = 1.0
    target_mi = convert_distance(distance_m, "mile")
    print(f"1.0 meters to miles: {target_mi}")
    distance_m = 3.28084
    target_ft = convert_distance(distance_m, "foot")
    print(f"3.28084 meters to feet: {target_ft}")
    distance_m = 10.0
    target_m = convert_distance(distance_m, "meter")
    print(f"10.0 meters to meters: {target_m}")
    try:
        convert_distance(5.0, 0)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error handled successfully: {e}")
    try:
        convert_distance(10.0, "lightyear")
    except ValueError as e:
        print(f"Error handled successfully: {e}")