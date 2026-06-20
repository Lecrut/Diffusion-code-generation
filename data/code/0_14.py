import math

_CONVERSION_FACTORS = {
    'm': 1.0,
    'km': 1000.0,
    'cm': 0.01,
    'mm': 0.001,
    'in': 0.0254,
    'ft': 0.3048,
    'yd': 0.9144,
    'mi': 1609.344
}

_UNIT_SYMBOLS = {
    'm': 'meters',
    'km': 'kilometers',
    'cm': 'centimeters',
    'mm': 'millimeters',
    'in': 'inches',
    'ft': 'feet',
    'yd': 'yards',
    'mi': 'miles'
}

def convert_length(value, from_unit, to_unit):
    if from_unit not in _CONVERSION_FACTORS:
        raise ValueError(f"Unknown from_unit: {from_unit}")
    if to_unit not in _CONVERSION_FACTORS:
        raise ValueError(f"Unknown to_unit: {to_unit}")
    
    value_in_meters = value * _CONVERSION_FACTORS[from_unit]
    result = value_in_meters / _CONVERSION_FACTORS[to_unit]
    
    return result

def format_result(value, from_unit, to_unit):
    result = convert_length(value, from_unit, to_unit)
    from_label = _UNIT_SYMBOLS[from_unit]
    to_label = _UNIT_SYMBOLS[to_unit]
    return f"{value} {from_label} = {result} {to_label}"

if __name__ == '__main__':
    print(format_result(1, 'm', 'ft'))
    print(format_result(1000, 'm', 'km'))
    print(format_result(1, 'mi', 'km'))
    print(format_result(12, 'in', 'cm'))
    print(format_result(1, 'km', 'mi'))