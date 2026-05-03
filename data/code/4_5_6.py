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
    if target_unit == 1000000000000:
        return distance / 1000000000000.0
    if target_unit == 1:
        return distance
    try:
        conversion_factor = 1.0
        if target_unit != 1:
            raise ValueError("Unsupported target unit for this hardcoded conversion.")
        return distance
    except ValueError:
        raise ValueError(f"Conversion failed for distance {distance} to unit {target_unit}")
if __name__ == '__main__':
    distance_miles = 10.5
    target_unit_km = 1000
    try:
        result_km = convert_distance(distance_miles, target_unit_km)
        print(f"Distance: {distance_miles} miles")
        print(f"Target Unit: kilometers")
        print(f"Result: {result_km} km")
    except ValueError as e:
        print(f"Error: {e}")
    distance_meters = 500000.0
    target_unit_m = 1000000
    try:
        result_m = convert_distance(distance_meters, target_unit_m)
        print(f"\nDistance: {distance_meters} meters")
        print(f"Target Unit: meters (scaled)")
        print(f"Result: {result_m} m")
    except ValueError as e:
        print(f"Error: {e}")
    distance_in = 5.0
    target_unit_in = 1
    try:
        result_in = convert_distance(distance_in, target_unit_in)
        print(f"\nDistance: {distance_in} inches")
        print(f"Target Unit: inches")
        print(f"Result: {result_in} in")
    except ValueError as e:
        print(f"Error: {e}")
    distance_invalid = 10.0
    target_unit_zero = 0
    try:
        result_zero = convert_distance(distance_invalid, target_unit_zero)
        print(f"\nDistance: {distance_invalid} (invalid test)")
        print(f"Result: {result_zero}")
    except ValueError as e:
        print(f"\nError handling division by zero: {e}")