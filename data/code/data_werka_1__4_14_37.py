def convert_distance(value, source_unit):
    conversion_factors = {'m': 1.0, 'km': 1000.0, 'mi': 1609.344, 'ft': 0.3048}
    target_units = ['m', 'km', 'mi', 'ft']
    if not isinstance(value, (int, float)):
        raise ValueError('Value must be a numeric type.')
    if source_unit not in conversion_factors:
        raise ValueError(f"Invalid source unit. Supported units are: {', '.join(target_units)}.")
    target_unit = next((unit for unit in target_units if unit != source_unit), None)
    if not target_unit:
        raise ValueError('Source and target units cannot be the same.')
    conversion_factor = conversion_factors[target_unit] / conversion_factors[source_unit]
    converted_value = value * conversion_factor
    return round(converted_value, 6)
if __name__ == '__main__':
    sample_values = [(100, 'm'), (5, 'km'), (3.10686, 'mi'), (3280.84, 'ft')]
    for value, source_unit in sample_values:
        try:
            result = convert_distance(value, source_unit)
            print(f'{value} {source_unit} is {result:.6f} of the target unit.')
        except ValueError as e:
            print(e)