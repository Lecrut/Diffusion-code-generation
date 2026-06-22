def convert_length(length_str, target_unit):
    conversion_factors = {'m': {'ft': 3.28084, 'in': 39.3701}, 'ft': {'m': 0.3048, 'in': 12}, 'in': {'m': 0.0254, 'ft': 0.083333}}
    try:
        value = float(length_str)
    except ValueError:
        raise ValueError('Invalid length value')
    source_unit = length_str.strip().replace(str(value), '').strip()
    if source_unit not in conversion_factors or target_unit not in conversion_factors[source_unit]:
        raise ValueError('Unsupported unit conversion')
    converted_value = value * conversion_factors[source_unit][target_unit]
    return converted_value
if __name__ == '__main__':
    length_str = '10m'
    target_unit = 'ft'
    result = convert_length(length_str, target_unit)
    print(f'{length_str} is {result} {target_unit}')