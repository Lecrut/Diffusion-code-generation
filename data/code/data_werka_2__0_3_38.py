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
    length_str = '10 m'
    target_unit = 'ft'
    try:
        result = convert_length(length_str, target_unit)
        print(result)
    except ValueError as e:
        print(e)