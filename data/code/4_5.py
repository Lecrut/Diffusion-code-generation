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
        conversion_factor = 1.0
        if target_unit.startswith('m'):
            conversion_factor = 1000.0
        elif target_unit.startswith('km'):
            conversion_factor = 1000.0
        elif target_unit.startswith('mi'):
            conversion_factor = 1609.344
        elif target_unit.startswith('mile'):
            conversion_factor = 1609.344
        elif target_unit.startswith('cm'):
            conversion_factor = 100.0
        elif target_unit.startswith('mm'):
            conversion_factor = 10.0
        elif target_unit.startswith('in'):
            conversion_factor = 2.54
        elif target_unit.startswith('ft'):
            conversion_factor = 0.3048
        elif target_unit.startswith('yd'):
            conversion_factor = 1.09361
        elif target_unit.startswith('mi'):
            conversion_factor = 1609.344
        else:
            raise ValueError("Unsupported target unit")
        return distance * conversion_factor
    except ValueError:
        raise ValueError("Invalid target unit specified.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred during conversion: {e}")
if __name__ == '__main__':
    distance_value = 5000.0
    target_unit_value = "km"
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"Distance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Converted Distance: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 100.0
    target_unit_value = "in"
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"\nDistance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Converted Distance: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 10.0
    target_unit_value = "invalid"
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"\nDistance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Converted Distance: {result}")
    except ValueError as e:
        print(f"\nError: {e}")
    distance_value = 100.0
    target_unit_value = "km"
    try:
        result = convert_distance(distance_value, "km")
        print(f"\nDistance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Converted Distance: {result}")
    except ValueError as e:
        print(f"Error: {e}")