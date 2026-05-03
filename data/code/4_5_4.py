import math
def convert_distance(distance, target_unit):
    if target_unit == 0:
        raise ValueError("Target unit cannot be zero.")
    if target_unit == 1:
        return distance
    distance_in_meters = distance
    if target_unit == 'm':
        return distance_in_meters
    elif target_unit == 'km':
        return distance_in_meters / 1000.0
    elif target_unit == 'mi':
        return distance_in_meters * 0.000621371
    else:
        raise ValueError(f"Unsupported target unit: {target_unit}")
if __name__ == '__main__':
    distance_value = 500.0
    target = 'km'
    try:
        result = convert_distance(distance_value, target)
        print(f"Distance: {distance_value} (Base Unit assumed: meters)")
        print(f"Target Unit: {target}")
        print(f"Converted Result: {result}")
        distance_value_2 = 1000.0
        target_2 = 'mi'
        result_2 = convert_distance(distance_value_2, target_2)
        print(f"\nDistance: {distance_value_2} (Base Unit assumed: meters)")
        print(f"Target Unit: {target_2}")
        print(f"Converted Result: {result_2}")
        try:
            convert_distance(10.0, 0)
        except ValueError as e:
            print(f"\nError handling test: {e}")
    except ValueError as e:
        print(f"An error occurred during execution: {e}")