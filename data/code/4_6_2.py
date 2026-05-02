import math
def convert_distance(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "m":
        if to_unit == "km":
            return value / 1000.0
        elif to_unit == "cm":
            return value * 100.0
        elif to_unit == "mm":
            return value * 10.0
        else:
            raise ValueError(f"Unsupported target unit: {to_unit}")
    elif from_unit == "km":
        if to_unit == "m":
            return value * 1000.0
        elif to_unit == "cm":
            return value * 100000.0
        elif to_unit == "mm":
            return value * 1000000.0
        else:
            raise ValueError(f"Unsupported target unit: {to_unit}")
    elif from_unit == "cm":
        if to_unit == "m":
            return value / 100.0
        elif to_unit == "km":
            return value / 1000000.0
        elif to_unit == "mm":
            return value / 10.0
        else:
            raise ValueError(f"Unsupported target unit: {to_unit}")
    elif from_unit == "mm":
        if to_unit == "m":
            return value / 1000.0
        elif to_unit == "km":
            return value / 1000000.0
        elif to_unit == "cm":
            return value / 10000.0
        else:
            raise ValueError(f"Unsupported target unit: {to_unit}")
    else:
        raise ValueError(f"Unsupported source unit: {from_unit}")
if __name__ == '__main__':
    distance_value = 500
    from_unit = "m"
    to_unit = "km"
    try:
        converted_value = convert_distance(distance_value, from_unit, to_unit)
        print(f"Input Distance: {distance_value} {from_unit}")
        print(f"Converted Distance: {converted_value:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 150
    from_unit = "cm"
    to_unit = "mm"
    try:
        converted_value = convert_distance(distance_value, from_unit, to_unit)
        print(f"\nInput Distance: {distance_value} {from_unit}")
        print(f"Converted Distance: {converted_value:.2f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 2.5
    from_unit = "km"
    to_unit = "m"
    try:
        converted_value = convert_distance(distance_value, from_unit, to_unit)
        print(f"\nInput Distance: {distance_value} {from_unit}")
        print(f"Converted Distance: {converted_value:.2f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 10
    from_unit = "m"
    to_unit = "cm"
    try:
        converted_value = convert_distance(distance_value, from_unit, to_unit)
        print(f"\nInput Distance: {distance_value} {from_unit}")
        print(f"Converted Distance: {converted_value:.2f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    distance_value = 10
    from_unit = "m"
    to_unit = "ft"
    try:
        converted_value = convert_distance(distance_value, from_unit, to_unit)
        print(f"\nInput Distance: {distance_value} {from_unit}")
        print(f"Converted Distance: {converted_value:.2f} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")