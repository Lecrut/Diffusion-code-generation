import math
def convert_units(value, from_unit, to_unit, conversion_factors):
    if from_unit == to_unit:
        return value
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("One or both units are not defined in the conversion factors.")
    value_in_base = value * conversion_factors[from_unit]
    value_in_target = value_in_base / conversion_factors[to_unit]
    return value_in_target
if __name__ == '__main__':
    conversion_factors = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "foot": 0.3048,
        "inch": 0.0254
    }
    value = 10.0
    from_unit = "kilometer"
    to_unit = "meter"
    result = convert_units(value, from_unit, to_unit, conversion_factors)
    print(f"{value} {from_unit} is equal to {result} {to_unit}")
    value = 500.0
    from_unit = "millimeter"
    to_unit = "meter"
    result = convert_units(value, from_unit, to_unit, conversion_factors)
    print(f"{value} {from_unit} is equal to {result} {to_unit}")
    value = 1.0
    from_unit = "mile"
    to_unit = "foot"
    result = convert_units(value, from_unit, to_unit, conversion_factors)
    print(f"{value} {from_unit} is equal to {result} {to_unit}")