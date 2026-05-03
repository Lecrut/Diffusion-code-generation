import math
def convert_units(value, from_unit, to_unit, conversion_factors):
    if from_unit == to_unit:
        return value
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("One or both units are not defined in the conversion factors.")
    base_value = 0
    if from_unit == 'base':
        base_value = value
    else:
        if from_unit not in conversion_factors:
            raise ValueError(f"Source unit {from_unit} not found.")
        base_value = value * conversion_factors[from_unit]
    if to_unit == 'base':
        return base_value
    else:
        if to_unit not in conversion_factors:
            raise ValueError(f"Target unit {to_unit} not found.")
        target_factor = conversion_factors[to_unit]
        if base_value == 0:
            return 0
        result = base_value / target_factor
        return result
if __name__ == '__main__':
    conversion_factors = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'mile': 1609.34,
        'foot': 0.3048,
        'inch': 0.0254
    }
    value_to_convert = 10
    from_unit = 'kilometer'
    to_unit = 'meter'
    try:
        result = convert_units(value_to_convert, from_unit, to_unit, conversion_factors)
        print(f"{value_to_convert} {from_unit} is equal to {result} {to_unit}")
        value_to_convert = 5
        from_unit = 'mile'
        to_unit = 'foot'
        result = convert_units(value_to_convert, from_unit, to_unit, conversion_factors)
        print(f"{value_to_convert} {from_unit} is equal to {result} {to_unit}")
        value_to_convert = 1
        from_unit = 'meter'
        to_unit = 'kilometer'
        result = convert_units(value_to_convert, from_unit, to_unit, conversion_factors)
        print(f"{value_to_convert} {from_unit} is equal to {result} {to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")