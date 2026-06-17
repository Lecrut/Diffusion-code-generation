import math
def convert_distance(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be numeric.")
    if from_unit == to_unit:
        return float(value)
    if from_unit == "meters" and to_unit == "feet":
        return value * 3.28084
    elif from_unit == "feet" and to_unit == "meters":
        return value / 3.28084
    elif from_unit == "kilometers" and to_unit == "meters":
        return value * 1000.0
    elif from_unit == "meters" and to_unit == "kilometers":
        return value / 1000.0
    elif from_unit == "miles" and to_unit == "kilometers":
        return value * 1.60934
    elif from_unit == "kilometers" and to_unit == "miles":
        return value / 1.60934
    else:
        raise ValueError(f"Unsupported unit conversion: {from_unit} to {to_unit}")
if __name__ == '__main__':
    test_cases = [
        (10, "meters", "feet"),
        (5, "miles", "kilometers"),
        (100, "kilometers", "meters"),
        (2, "feet", "meters"),
        (10, "meters", "meters"),
        (1, "miles", "miles")
    ]
    for value, from_u, to_u in test_cases:
        try:
            result = convert_distance(value, from_u, to_u)
            print(f"Converting {value} {from_u} to {to_u}: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error processing ({value}, {from_u}, {to_u}): {e}")
    error_cases = [
        (10.5, "meters", "lightyears"),
        ("invalid", "meters", "feet"),
        (5, "yards", "miles")
    ]
    print("\n--- Error Testing ---")
    for value, from_u, to_u in error_cases:
        try:
            result = convert_distance(value, from_u, to_u)
            print(f"Unexpected success for ({value}, {from_u}, {to_u}): {result}")
        except (TypeError, ValueError) as e:
            print(f"Successfully caught expected error for ({value}, {from_u}, {to_u}): {e}")