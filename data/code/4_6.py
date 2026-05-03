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