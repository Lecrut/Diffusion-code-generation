def convert_length(value, from_unit, to_unit):
    CONVERSION_FACTORS = {'m': 1, 'cm': 0.01, 'mm': 0.001, 'km': 1000, 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.34}
    if from_unit not in CONVERSION_FACTORS or to_unit not in CONVERSION_FACTORS:
        raise ValueError('Unsupported unit')
    value_in_meters = value * CONVERSION_FACTORS[from_unit]
    converted_value = value_in_meters / CONVERSION_FACTORS[to_unit]
    return converted_value
if __name__ == '__main__':
    sample_length = 500
    source_unit = 'mm'
    target_unit = 'cm'
    result = convert_length(sample_length, source_unit, target_unit)
    print(result)