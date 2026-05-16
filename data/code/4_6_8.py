import math
def convert_distance(distance, from_unit, to_unit):
    if from_unit == to_unit:
        return distance
    if from_unit == "m" and to_unit == "km":
        return distance / 1000.0
    elif from_unit == "km" and to_unit == "m":
        return distance * 1000.0
    elif from_unit == "cm" and to_unit == "m":
        return distance / 100.0
    elif from_unit == "m" and to_unit == "cm":
        return distance * 100.0
    elif from_unit == "in" and to_unit == "cm":
        return distance * 2.54
    elif from_unit == "cm" and to_unit == "in":
        return distance / 2.54
    elif from_unit == "mi" and to_unit == "km":
        return distance * 1.60934
    elif from_unit == "km" and to_unit == "mi":
        return distance / 1.60934
    else:
        raise ValueError("Unsupported unit conversion.")
if __name__ == '__main__':
    sample_distance = 100
    sample_from_unit = "m"
    sample_to_unit = "km"
    try:
        converted_value = convert_distance(sample_distance, sample_from_unit, sample_to_unit)
        print(f"Input Distance: {sample_distance} {sample_from_unit}")
        print(f"Converted Value: {converted_value} {sample_to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("-" * 20)
    sample_distance_2 = 100
    sample_from_unit_2 = "mi"
    sample_to_unit_2 = "km"
    try:
        converted_value_2 = convert_distance(sample_distance_2, sample_from_unit_2, sample_to_unit_2)
        print(f"Input Distance: {sample_distance_2} {sample_from_unit_2}")
        print(f"Converted Value: {converted_value_2} {sample_to_unit_2}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("-" * 20)
    sample_distance_3 = 50
    sample_from_unit_3 = "cm"
    sample_to_unit_3 = "in"
    try:
        converted_value_3 = convert_distance(sample_distance_3, sample_from_unit_3, sample_to_unit_3)
        print(f"Input Distance: {sample_distance_3} {sample_from_unit_3}")
        print(f"Converted Value: {converted_value_3} {sample_to_unit_3}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("-" * 20)
    sample_distance_4 = 10
    sample_from_unit_4 = "m"
    sample_to_unit_4 = "ft"
    try:
        converted_value_4 = convert_distance(sample_distance_4, sample_from_unit_4, sample_to_unit_4)
        print(f"Input Distance: {sample_distance_4} {sample_from_unit_4}")
        print(f"Converted Value: {converted_value_4} {sample_to_unit_4}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")