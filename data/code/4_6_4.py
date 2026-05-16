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
    elif from_unit == "meter" and to_unit == "foot":
        return distance * 3.28084
    elif from_unit == "foot" and to_unit == "meter":
        return distance / 3.28084
    elif from_unit == "mile" and to_unit == "foot":
        return distance * 5280.0
    elif from_unit == "foot" and to_unit == "mile":
        return distance / 5280.0
    else:
        raise ValueError("Unsupported unit conversion.")
if __name__ == '__main__':
    sample_distance = 10
    sample_from_unit = "mile"
    sample_to_unit = "kilometer"
    try:
        converted_value = convert_distance(sample_distance, sample_from_unit, sample_to_unit)
        print(f"Original Distance: {sample_distance} {sample_from_unit}")
        print(f"Converted Distance: {converted_value:.4f} {sample_to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    sample_distance_2 = 100
    sample_from_unit_2 = "meter"
    sample_to_unit_2 = "foot"
    try:
        converted_value_2 = convert_distance(sample_distance_2, sample_from_unit_2, sample_to_unit_2)
        print(f"\nOriginal Distance: {sample_distance_2} {sample_from_unit_2}")
        print(f"Converted Distance: {converted_value_2:.4f} {sample_to_unit_2}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    sample_distance_3 = 5
    sample_from_unit_3 = "meter"
    sample_to_unit_3 = "meter"
    try:
        converted_value_3 = convert_distance(sample_distance_3, sample_from_unit_3, sample_to_unit_3)
        print(f"\nOriginal Distance: {sample_distance_3} {sample_from_unit_3}")
        print(f"Converted Distance: {converted_value_3:.4f} {sample_to_unit_3}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")