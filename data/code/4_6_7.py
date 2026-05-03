import math
def convert_distance(distance, from_unit, to_unit):
    if from_unit == to_unit:
        return distance
    if from_unit == "meter" and to_unit == "kilometer":
        return distance / 1000.0
    elif from_unit == "kilometer" and to_unit == "meter":
        return distance * 1000.0
    elif from_unit == "mile" and to_unit == "kilometer":
        return distance * 1.60934
    elif from_unit == "kilometer" and to_unit == "mile":
        return distance / 1.60934
    elif from_unit == "meter" and to_unit == "inch":
        return distance * 39.3701
    elif from_unit == "inch" and to_unit == "meter":
        return distance / 39.3701
    else:
        raise ValueError("Unsupported unit conversion.")
if __name__ == '__main__':
    sample_distance = 10
    from_unit = "meter"
    to_unit = "kilometer"
    try:
        converted_value = convert_distance(sample_distance, from_unit, to_unit)
        print(f"Original Distance: {sample_distance} {from_unit}")
        print(f"Converted Distance: {converted_value:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    sample_distance_2 = 1
    from_unit_2 = "mile"
    to_unit_2 = "kilometer"
    try:
        converted_value_2 = convert_distance(sample_distance_2, from_unit_2, to_unit_2)
        print(f"\nOriginal Distance: {sample_distance_2} {from_unit_2}")
        print(f"Converted Distance: {converted_value_2:.4f} {to_unit_2}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    sample_distance_3 = 100
    from_unit_3 = "meter"
    to_unit_3 = "inch"
    try:
        converted_value_3 = convert_distance(sample_distance_3, from_unit_3, to_unit_3)
        print(f"\nOriginal Distance: {sample_distance_3} {from_unit_3}")
        print(f"Converted Distance: {converted_value_3:.4f} {to_unit_3}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")