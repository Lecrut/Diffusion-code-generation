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
    if target_unit == 10000000000:
        return distance / 10000000000.0
    if target_unit == 1:
        return distance
    if target_unit == 0:
        raise ValueError("Target unit cannot be zero.")
    return distance / target_unit
if __name__ == '__main__':
    distance_miles = 10.5
    target_unit_km = 1000.0
    try:
        result_km = convert_distance(distance_miles, target_unit_km)
        print(f"Distance: {distance_miles} miles")
        print(f"Target Unit: {target_unit_km}")
        print(f"Result: {result_km} km")
    except ValueError as e:
        print(f"Error: {e}")
    distance_meters = 5000.0
    target_unit_m = 1.0
    try:
        result_m = convert_distance(distance_meters, target_unit_m)
        print(f"\nDistance: {distance_meters} meters")
        print(f"Target Unit: {target_unit_m}")
        print(f"Result: {result_m} m")
    except ValueError as e:
        print(f"Error: {e}")
    distance_feet = 100.0
    target_unit_ft = 1.0
    try:
        result_ft = convert_distance(distance_feet, target_unit_ft)
        print(f"\nDistance: {distance_feet} feet")
        print(f"Target Unit: {target_unit_ft}")
        print(f"Result: {result_ft} ft")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        convert_distance(10.0, 0)
    except ValueError as e:
        print("\nTesting division by zero handling:")
        print(f"Caught expected error: {e}")