import math
def convert_units(value, from_unit, to_unit, conversion_factors):
    if from_unit == to_unit:
        return value
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("One or both units not found in conversion factors.")
    value_in_base = value * conversion_factors[from_unit]
    value_in_target = value_in_base / conversion_factors[to_unit]
    return value_in_target
if __name__ == '__main__':
    BASE_UNIT = "m"
    conversion_factors = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "in": 0.0254,
        "ft": 0.3048,
        "mi": 1609.34
    }
    value_to_convert = 5.28
    from_unit = "mi"
    to_unit = "km"
    try:
        result = convert_units(value_to_convert, from_unit, to_unit, conversion_factors)
        print(f"{value_to_convert} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    value_to_convert = 100.0
    from_unit = "cm"
    to_unit = "m"
    try:
        result = convert_units(value_to_convert, from_unit, to_unit, conversion_factors)
        print(f"{value_to_convert} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    value_to_convert = 10.0
    from_unit = "ft"
    to_unit = "in"
    try:
        result = convert_units(value_to_convert, from_unit, to_unit, conversion_factors)
        print(f"{value_to_convert} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")