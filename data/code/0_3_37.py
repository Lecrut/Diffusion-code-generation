def convert_length(length_str, target_unit):
    conversion_factors = {'m': {'ft': 3.28084, 'in': 39.3701}, 'ft': {'m': 0.3048, 'in': 12}, 'in': {'m': 0.0254, 'ft': 0.083333}}
    try:
        value = float(length_str)
    except ValueError:
        raise ValueError('Invalid length value')
    if length_str.endswith('m'):
        source_unit = 'm'
    elif length_str.endswith('ft'):
        source_unit = 'ft'
    elif length_str.endswith('in'):
        source_unit = 'in'
    else:
        raise ValueError('Invalid unit in length string')
    if target_unit not in conversion_factors[source_unit]:
        raise ValueError(f'Conversion from {source_unit} to {target_unit} is not supported')
    converted_value = value * conversion_factors[source_unit][target_unit]
    return f'{converted_value}{target_unit}'
if __name__ == '__main__':
    print(convert_length('10m', 'ft'))
    print(convert_length('50ft', 'in'))
    print(convert_length('100in', 'm'))