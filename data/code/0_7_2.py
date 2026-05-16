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
    CONVERSION_FACTORS = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.34,
        "ft": 3.28084,
        "in": 0.0254
    }
    value_to_convert = 5
    from_unit_val = "km"
    to_unit_val = "m"
    print(f"Converting {value_to_convert} {from_unit_val} to {to_unit_val}")
    try:
        result = convert_units(value_to_convert, from_unit_val, to_unit_val, CONVERSION_FACTORS)
        print(f"Result: {result:.4f} {BASE_UNIT}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    value_to_convert = 100
    from_unit_val = "ft"
    to_unit_val = "in"
    print(f"Converting {value_to_convert} {from_unit_val} to {to_unit_val}")
    try:
        result = convert_units(value_to_convert, from_unit_val, to_unit_val, CONVERSION_FACTORS)
        print(f"Result: {result:.4f} {BASE_UNIT}")
    except ValueError as e:
        print(f"Error: {e}")
    print("-" * 20)
    value_to_convert = 10
    from_unit_val = "mm"
    to_unit_val = "km"
    print(f"Converting {value_to_convert} {from_unit_val} to {to_unit_val}")
    try:
        result = convert_units(value_to_convert, from_unit_val, to_unit_val, CONVERSION_FACTORS)
        print(f"Result: {result:.6f} {BASE_UNIT}")
    except ValueError as e:
        print(f"Error: {e}")