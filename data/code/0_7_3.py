import math
def convert_units(value, from_unit, to_unit, conversion_factors):
    if from_unit == to_unit:
        return value
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("One or both units not found in conversion factors.")
    to_base = 1.0
    if from_unit == 'base':
        to_base = value
    else:
        from_factor = conversion_factors[from_unit]
        to_factor = conversion_factors[to_unit]
        to_base = value / from_factor
        to_base *= to_factor
    return to_base
def optimized_unit_conversion(value, from_unit, to_unit, conversion_factors):
    if from_unit == to_unit:
        return value
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("One or both units not found in conversion factors.")
    if from_unit == 'base':
        factor_from = 1.0
    else:
        factor_from = conversion_factors[from_unit]
    if to_unit == 'base':
        return value * factor_from
    else:
        factor_to = conversion_factors[to_unit]
        return value / factor_from * factor_to
if __name__ == '__main__':
    conversion_factors = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'mile': 1609.34,
        'foot': 0.3048,
        'inch': 0.0254
    }
    value = 10.0
    from_unit = 'mile'
    to_unit = 'meter'
    result = optimized_unit_conversion(value, from_unit, to_unit, conversion_factors)
    print(f"Conversion of {value} {from_unit} to meters: {result}")
    value = 1000.0
    from_unit = 'kilometer'
    to_unit = 'mile'
    result = optimized_unit_conversion(value, from_unit, to_unit, conversion_factors)
    print(f"Conversion of {value} {from_unit} to miles: {result}")
    value = 10.0
    from_unit = 'foot'
    to_unit = 'inch'
    result = optimized_unit_conversion(value, from_unit, to_unit, conversion_factors)
    print(f"Conversion of {value} {from_unit} to inches: {result}")
    value = 5.0
    from_unit = 'meter'
    to_unit = 'kilometer'
    result = optimized_unit_conversion(value, from_unit, to_unit, conversion_factors)
    print(f"Conversion of {value} {from_unit} to kilometers: {result}")
    value = 10.0
    from_unit = 'meter'
    to_unit = 'meter'
    result = optimized_unit_conversion(value, from_unit, to_unit, conversion_factors)
    print(f"Conversion of {value} {from_unit} to meters: {result}")