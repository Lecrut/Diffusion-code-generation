import math
def convert_distance(distance, from_unit, to_unit):
    if from_unit == to_unit:
        return distance
    if from_unit == "meter" and to_unit == "kilometer":
        return distance / 1000
    elif from_unit == "kilometer" and to_unit == "meter":
        return distance * 1000
    elif from_unit == "mile" and to_unit == "kilometer":
        return distance * 1.60934
    elif from_unit == "kilometer" and to_unit == "mile":
        return distance / 1.60934
    elif from_unit == "meter" and to_unit == "centimeter":
        return distance * 100
    elif from_unit == "centimeter" and to_unit == "meter":
        return distance / 100
    else:
        raise ValueError("Unsupported unit conversion.")
if __name__ == '__main__':
    sample_distance = 10
    sample_from_unit = "mile"
    sample_to_unit = "kilometer"
    try:
        converted_value = convert_distance(sample_distance, sample_from_unit, sample_to_unit)
        print(f"Input Distance: {sample_distance} {sample_from_unit}")
        print(f"Converted Value: {converted_value:.4f} {sample_to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    sample_distance_2 = 500
    sample_from_unit_2 = "meter"
    sample_to_unit_2 = "centimeter"
    try:
        converted_value_2 = convert_distance(sample_distance_2, sample_from_unit_2, sample_to_unit_2)
        print(f"\nInput Distance: {sample_distance_2} {sample_from_unit_2}")
        print(f"Converted Value: {converted_value_2:.2f} {sample_to_unit_2}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    sample_distance_3 = 100
    sample_from_unit_3 = "mile"
    sample_to_unit_3 = "meter"
    try:
        converted_value_3 = convert_distance(sample_distance_3, sample_from_unit_3, sample_to_unit_3)
        print(f"\nInput Distance: {sample_distance_3} {sample_from_unit_3}")
        print(f"Converted Value: {converted_value_3:.2f} {sample_to_unit_3}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")