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
            if target_unit > 0:
                return distance / target_unit
            else:
                raise ValueError("Target unit must be positive.")
        return distance
    except ZeroDivisionError:
        raise ValueError("Division by zero occurred during conversion.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    distance_miles = 10.5
    target_unit_km = 1000
    try:
        result_km = convert_distance(distance_miles, target_unit_km)
        print(f"Distance: {distance_miles} miles")
        print(f"Target Unit: {target_unit_km}")
        print(f"Result: {result_km} km")
    except ValueError as e:
        print(f"Error: {e}")
    distance_meters = 5000.0
    target_unit_m = 1000000
    try:
        result_m = convert_distance(distance_meters, target_unit_m)
        print(f"\nDistance: {distance_meters} meters")
        print(f"Target Unit: {target_unit_m}")
        print(f"Result: {result_m} m")
    except ValueError as e:
        print(f"Error: {e}")
    distance_miles_to_miles = 20.0
    target_unit_miles = 1
    try:
        result_miles = convert_distance(distance_miles_to_miles, target_unit_miles)
        print(f"\nDistance: {distance_miles_to_miles} miles")
        print(f"Target Unit: {target_unit_miles}")
        print(f"Result: {result_miles} miles")
    except ValueError as e:
        print(f"Error: {e}")
    distance_error = 10.0
    target_unit_error = 0
    try:
        result_error = convert_distance(distance_error, target_unit_error)
        print(f"\nDistance: {distance_error} units")
        print(f"Target Unit: {target_unit_error}")
        print(f"Result: {result_error} units")
    except ValueError as e:
        print(f"\nError Handling Test:")
        print(f"Error: {e}")