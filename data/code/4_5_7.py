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
    try:
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
        if target_unit == 0:
            raise ZeroDivisionError
        return distance / target_unit
    except ZeroDivisionError:
        raise ValueError("Invalid target unit: Division by zero attempted.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    distance_miles = 10.5
    target_unit_km = 1000.0
    target_unit_miles = 1.0
    target_unit_invalid = 0.0
    try:
        result_km = convert_distance(distance_miles, target_unit_km)
        print(f"Distance: {distance_miles} miles, Target: {target_unit_km} (km) -> {result_km} km")
        result_miles = convert_distance(distance_miles, target_unit_miles)
        print(f"Distance: {distance_miles} miles, Target: {target_unit_miles} (miles) -> {result_miles} miles")
        try:
            convert_distance(distance_miles, target_unit_invalid)
        except ValueError as e:
            print(f"Error handling for invalid unit: {e}")
    except ValueError as e:
        print(f"Conversion failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during testing: {e}")