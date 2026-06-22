def convert_distance(value, source_unit):
    valid_units = ('meters', 'kilometers', 'miles', 'feet')
    if not isinstance(source_unit, str) or source_unit not in valid_units:
        raise ValueError("Invalid unit. Must be one of: meters, kilometers, miles, feet")
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if isinstance(value, bool):
        raise TypeError("Value must be a number")
    meters_to_kilometers = 0.001
    meters_to_miles = 0.000621371
    meters_to_feet = 3.28084
    value_in_meters = value
    if source_unit == 'kilometers':
        value_in_meters = value / meters_to_kilometers
    elif source_unit == 'miles':
        value_in_meters = value / meters_to_miles
    elif source_unit == 'feet':
        value_in_meters = value / meters_to_feet
    results = {
        'meters': value_in_meters,
        'kilometers': value_in_meters * meters_to_kilometers,
        'miles': value_in_meters * meters_to_miles,
        'feet': value_in_meters * meters_to_feet
    }
    return {unit: round(val, 6) for unit, val in results.items()}

if __name__ == '__main__':
    sample_value = 100
    sample_unit = 'meters'
    result = convert_distance(sample_value, sample_unit)
    print(result)