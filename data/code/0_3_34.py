def convert_length(value_str, target_unit_code):
    conversions = {'m': 1.0, 'cm': 100, 'mm': 1000, 'km': 0.001, 'in': 39.3701, 'ft': 3.28084, 'yd': 1.09361, 'mi': 0.000621371}
    parts = value_str.split()
    if len(parts) != 2:
        raise ValueError("Input must be in the format 'value unit'")
    try:
        value = float(parts[0])
    except ValueError:
        raise ValueError('The first part of the input must be a valid number')
    source_unit_code = parts[1]
    if source_unit_code not in conversions:
        raise ValueError(f'Unknown source unit: {source_unit_code}')
    if target_unit_code not in conversions:
        raise ValueError(f'Unknown target unit: {target_unit_code}')
    value_in_meters = value * conversions[source_unit_code]
    converted_value = value_in_meters / conversions[target_unit_code]
    return converted_value
if __name__ == '__main__':
    sample_values = [('10 m', 'ft'), ('5.5 cm', 'mm'), ('2 km', 'mi'), ('100 in', 'yd'), ('3 yd', 'm')]
    for value_str, target_unit_code in sample_values:
        try:
            result = convert_length(value_str, target_unit_code)
            print(f'{value_str} is {result:.4f} {target_unit_code}')
        except ValueError as e:
            print(e)