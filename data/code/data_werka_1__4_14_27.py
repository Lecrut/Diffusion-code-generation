def convert_distance(value, source_unit):
    conversion_factors = {'meters_to_kilometers': 0.001, 'meters_to_miles': 0.000621371, 'meters_to_feet': 3.28084, 'kilometers_to_meters': 1000, 'kilometers_to_miles': 0.621371, 'kilometers_to_feet': 3280.84, 'miles_to_meters': 1609.34, 'miles_to_kilometers': 1.60934, 'miles_to_feet': 5280, 'feet_to_meters': 0.3048, 'feet_to_kilometers': 0.0003048, 'feet_to_miles': 0.000189394}
    valid_units = ['meters', 'kilometers', 'miles', 'feet']
    if source_unit not in valid_units:
        raise ValueError('Invalid source unit. Choose from: meters, kilometers, miles, feet.')
    converted_values = {}
    for target_unit in valid_units:
        if source_unit != target_unit:
            key = f'{source_unit}_to_{target_unit}'
            conversion_factor = conversion_factors[key]
            converted_value = value * conversion_factor
            converted_values[target_unit] = round(converted_value, 6)
    return converted_values
if __name__ == '__main__':
    sample_value = 100
    sample_unit = 'meters'
    result = convert_distance(sample_value, sample_unit)
    print(result)