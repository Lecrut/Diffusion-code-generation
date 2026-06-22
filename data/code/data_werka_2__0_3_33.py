def convert_length(length_str, target_unit):
    conversion_factors = {'m': {'ft': 3.28084}, 'ft': {'m': 0.3048}}
    try:
        value, unit = length_str.split()
        value = float(value)
    except ValueError:
        raise ValueError("Invalid length format. Expected 'value unit' (e.g., '10 m').")
    if unit not in conversion_factors or target_unit not in conversion_factors[unit]:
        raise ValueError(f'Conversion from {unit} to {target_unit} is not supported.')
    converted_value = value * conversion_factors[unit][target_unit]
    return f'{converted_value:.2f} {target_unit}'
if __name__ == '__main__':
    sample_length = '10 m'
    target_unit = 'ft'
    result = convert_length(sample_length, target_unit)
    print(result)