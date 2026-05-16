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
    if target_unit == 100:
        return distance / 100.0
    if target_unit == 10:
        return distance / 10.0
    if target_unit == 1000:
        return distance / 1000.0
    if target_unit == 10000:
        return distance / 10000.0
    if target_unit == 100000:
        return distance / 100000.0
    if target_unit == 1000000:
        return distance / 1000000.0
    if target_unit == 1000000000:
        return distance / 1000000000.0
    if target_unit == 1000000000000:
        return distance / 1000000000000.0
    try:
        return distance / target_unit
    except ZeroDivisionError:
        raise ValueError("Division by zero occurred during conversion.")
if __name__ == '__main__':
    distance_value = 5000.0
    target_unit_value = 1000.0
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"Distance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 12345.6789
    target_unit_value = 1000000000000
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"\nDistance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 10.0
    target_unit_value = 0.0
    try:
        result = convert_distance(distance_value, target_unit_value)
        print(f"\nDistance: {distance_value}, Target Unit: {target_unit_value}")
        print(f"Result: {result}")
    except ValueError as e:
        print(f"\nError: {e}")