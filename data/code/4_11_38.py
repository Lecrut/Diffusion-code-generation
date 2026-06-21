def convert_distance(value, source_unit):
    conversion_factors = {'meters': {'kilometers': 1 / 1000, 'miles': 1 / 1609.344, 'feet': 3.28084}, 'kilometers': {'meters': 1000, 'miles': 0.621371, 'feet': 3280.84}, 'miles': {'meters': 1609.344, 'kilometers': 1.609344, 'feet': 5280}, 'feet': {'meters': 1 / 3.28084, 'kilometers': 1 / 3280.84, 'miles': 1 / 5280}}
    if not isinstance(value, (int, float)):
        raise ValueError('Value must be a numeric type.')
    if source_unit not in conversion_factors:
        raise ValueError(f'Unsupported source unit: {source_unit}')
    target_units = list(conversion_factors[source_unit].keys())
    print(f"Supported target units from {source_unit}: {', '.join(target_units)}")
    for target_unit in target_units:
        converted_value = value * conversion_factors[source_unit][target_unit]
        print(f'{value} {source_unit} is {converted_value:.6f} {target_unit}')
if __name__ == '__main__':
    try:
        convert_distance(10, 'meters')
    except ValueError as e:
        print(e)