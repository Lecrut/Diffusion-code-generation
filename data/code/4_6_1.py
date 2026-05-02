import math
def convert_distance(distance, from_unit, to_unit):
    if from_unit == to_unit:
        return distance
    if from_unit == "meter":
        if to_unit == "kilometer":
            return distance / 1000
        elif to_unit == "centimeter":
            return distance * 100
        elif to_unit == "millimeter":
            return distance * 1000
        else:
            raise ValueError("Unsupported target unit.")
    elif from_unit == "kilometer":
        if to_unit == "meter":
            return distance * 1000
        elif to_unit == "centimeter":
            return distance * 100000
        elif to_unit == "millimeter":
            return distance * 1000000
        else:
            raise ValueError("Unsupported target unit.")
    elif from_unit == "meter":
        if to_unit == "mile":
            return distance / 1609.34
        elif to_unit == "yard":
            return distance / 0.9144
        elif to_unit == "foot":
            return distance / 0.3048
        else:
            raise ValueError("Unsupported target unit.")
    elif from_unit == "mile":
        if to_unit == "kilometer":
            return distance * 1.60934
        elif to_unit == "meter":
            return distance * 1609.34
        elif to_unit == "yard":
            return distance * 1760.0
        elif to_unit == "foot":
            return distance * 5280.0
        else:
            raise ValueError("Unsupported target unit.")
    elif from_unit == "foot":
        if to_unit == "meter":
            return distance * 0.3048
        elif to_unit == "yard":
            return distance / 0.9144
        elif to_unit == "mile":
            return distance / 1609.34
        else:
            raise ValueError("Unsupported target unit.")
    else:
        raise ValueError("Unsupported source unit.")
if __name__ == '__main__':
    distance_value = 100
    from_unit_value = "meter"
    to_unit_value = "kilometer"
    try:
        converted_result = convert_distance(distance_value, from_unit_value, to_unit_value)
        print(f"Input Distance: {distance_value} {from_unit_value}")
        print(f"Converted Distance: {converted_result} {to_unit_value}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    distance_value = 1
    from_unit_value = "mile"
    to_unit_value = "foot"
    try:
        converted_result = convert_distance(distance_value, from_unit_value, to_unit_value)
        print(f"\nInput Distance: {distance_value} {from_unit_value}")
        print(f"Converted Distance: {converted_result} {to_unit_value}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    distance_value = 500
    from_unit_value = "meter"
    to_unit_value = "millimeter"
    try:
        converted_result = convert_distance(distance_value, from_unit_value, to_unit_value)
        print(f"\nInput Distance: {distance_value} {from_unit_value}")
        print(f"Converted Distance: {converted_result} {to_unit_value}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")