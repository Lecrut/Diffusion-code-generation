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
        if target_unit == "miles":
            conversion_factor = 1609.344
        elif target_unit == "kilometers":
            conversion_factor = 1000.0
        elif target_unit == "meters":
            conversion_factor = 100.0
        elif target_unit == "feet":
            conversion_factor = 3.28084
        elif target_unit == "inches":
            conversion_factor = 39.3701
        else:
            raise ValueError("Unsupported target unit")
        return distance * conversion_factor
    except ValueError:
        raise ValueError("Invalid conversion requested.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    distance_value = 1000.0
    target_unit_value = "kilometers"
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"Distance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Converted Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 10.0
    target_unit_value = "miles"
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"\nDistance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Converted Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 500.0
    target_unit_value = "meters"
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"\nDistance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Converted Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 10.0
    target_unit_value = "invalid_unit"
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"\nDistance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Converted Result: {result}")
    except ValueError as e:
        print(f"\nError: {e}")
    distance_value = 10.0
    target_unit_value = "0"
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"\nDistance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Converted Result: {result}")
    except ValueError as e:
        print(f"\nError: {e}")