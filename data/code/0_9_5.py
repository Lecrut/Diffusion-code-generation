import math
def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversion_factors = {
        'm': 1.0,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'm': 1.0,
        'cm': 0.01,
        'mm': 0.001
    }
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported unit provided.")
    value_in_meters = 0.0
    if from_unit == 'm':
        value_in_meters = value
    elif from_unit == 'km':
        value_in_meters = value * 1000.0
    elif from_unit == 'cm':
        value_in_meters = value * 0.01
    elif from_unit == 'mm':
        value_in_meters = value * 0.001
    else:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit == 'm':
        return value_in_meters
    elif to_unit == 'km':
        return value_in_meters / 1000.0
    elif to_unit == 'cm':
        return value_in_meters / 0.01
    elif to_unit == 'mm':
        return value_in_meters / 0.001
    else:
        raise ValueError(f"Unknown target unit: {to_unit}")
if __name__ == '__main__':
    length = 1500
    from_unit = 'mm'
    to_unit = 'km'
    try:
        result = convert_length(length, from_unit, to_unit)
        print(f"Converting {length} {from_unit} to {to_unit}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    length = 2.5
    from_unit = 'm'
    to_unit = 'cm'
    try:
        result = convert_length(length, from_unit, to_unit)
        print(f"Converting {length} {from_unit} to {to_unit}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    length = 500
    from_unit = 'km'
    to_unit = 'm'
    try:
        result = convert_length(length, from_unit, to_unit)
        print(f"Converting {length} {from_unit} to {to_unit}: {result}")
    except ValueError as e:
        print(f"Error: {e}")