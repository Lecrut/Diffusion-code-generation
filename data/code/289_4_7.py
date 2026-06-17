import math
def convert_distance(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be numeric.")
    if from_unit == to_unit:
        return float(value)
    if from_unit == "m" and to_unit == "km":
        return value / 1000.0
    elif from_unit == "km" and to_unit == "m":
        return value * 1000.0
    elif from_unit == "cm" and to_unit == "m":
        return value / 100.0
    elif from_unit == "m" and to_unit == "cm":
        return value * 100.0
    elif from_unit == "in" and to_unit == "cm":
        return value * 2.54
    elif from_unit == "cm" and to_unit == "in":
        return value / 2.54
    else:
        raise ValueError(f"Unsupported conversion: {from_unit} to {to_unit}")
if __name__ == '__main__':
    test_cases = [
        (10, "m", "km"),
        (5000, "km", "m"),
        (2.54, "in", "cm"),
        (100, "cm", "m"),
        (10, "m", "m"),
        (10, "km", "m"),
        (10, "ft", "m")                                                             
    ]
    for value, from_u, to_u in test_cases:
        try:
            result = convert_distance(value, from_u, to_u)
            print(f"Converting {value} {from_u} to {to_u}: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error converting {value} {from_u} to {to_u}: {e}")