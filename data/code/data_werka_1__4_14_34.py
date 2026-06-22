def convert_distance(value, source_unit):
    conversion_factors = {'meters_to_kilometers': 0.001, 'meters_to_miles': 0.000621371, 'meters_to_feet': 3.28084, 'kilometers_to_meters': 1000, 'kilometers_to_miles': 0.621371, 'kilometers_to_feet': 3280.84, 'miles_to_meters': 1609.34, 'miles_to_kilometers': 1.60934, 'miles_to_feet': 5280, 'feet_to_meters': 0.3048, 'feet_to_kilometers': 0.0003048, 'feet_to_miles': 0.000189394}
    valid_units = ['meters', 'kilometers', 'miles', 'feet']
    if source_unit not in valid_units:
        raise ValueError('Invalid source unit')
    if source_unit == 'meters':
        converted_value = {'kilometers': value * conversion_factors['meters_to_kilometers'], 'miles': value * conversion_factors['meters_to_miles'], 'feet': value * conversion_factors['meters_to_feet']}
    elif source_unit == 'kilometers':
        converted_value = {'meters': value * conversion_factors['kilometers_to_meters'], 'miles': value * conversion_factors['kilometers_to_miles'], 'feet': value * conversion_factors['kilometers_to_feet']}
    elif source_unit == 'miles':
        converted_value = {'meters': value * conversion_factors['miles_to_meters'], 'kilometers': value * conversion_factors['miles_to_kilometers'], 'feet': value * conversion_factors['miles_to_feet']}
    elif source_unit == 'feet':
        converted_value = {'meters': value * conversion_factors['feet_to_meters'], 'kilometers': value * conversion_factors['feet_to_kilometers'], 'miles': value * conversion_factors['feet_to_miles']}
    return {unit: round(converted_value[unit], 6) for unit in valid_units if unit != source_unit}
if __name__ == '__main__':
    sample_values = [(100, 'meters'), (5, 'kilometers'), (2.5, 'miles'), (3000, 'feet')]
    for value, unit in sample_values:
        print(convert_distance(value, unit))