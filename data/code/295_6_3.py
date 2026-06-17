import math
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        ('meter', 'foot'): 3.28084,
        ('foot', 'meter'): 0.3048,
        ('kilometer', 'meter'): 1000,
        ('meter', 'kilometer'): 0.001,
        ('inch', 'centimeter'): 2.54,
        ('centimeter', 'inch'): 1 / 2.54
    }
    key = (from_unit, to_unit)
    if key in conversion_factors:
        return value * conversion_factors[key]
    elif from_unit == to_unit:
        return value
    else:
        return "Conversion not supported for this pair."
if __name__ == '__main__':
    initial_value = 10
    from_unit = "meter"
    to_unit = "foot"
    result = convert_units(initial_value, from_unit, to_unit)
    print(f"Initial Value: {initial_value}")
    print(f"Conversion Pair: {from_unit} to {to_unit}")
    print(f"Result: {result:.4f}")