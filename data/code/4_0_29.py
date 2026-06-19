def convert_distance(value, from_unit, to_unit):
    conversion_factors = {'m_to_km': 0.001, 'km_to_m': 1000, 'm_to_mi': 0.000621371, 'mi_to_m': 1609.34, 'km_to_mi': 0.621371, 'mi_to_km': 1.60934}
    valid_units = ['m', 'km', 'mi']
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("Invalid unit. Please use 'm' for meters, 'km' for kilometers, or 'mi' for miles.")
    conversion_key = f'{from_unit}_to_{to_unit}'
    if conversion_key in conversion_factors:
        return value * conversion_factors[conversion_key]
    else:
        raise ValueError('Conversion not supported between the given units.')
if __name__ == '__main__':
    distance_meters = 1000
    distance_kilometers = 5
    distance_miles = 3
    converted_km = convert_distance(distance_meters, 'm', 'km')
    print(f'{distance_meters} meters is {converted_km} kilometers')
    converted_mi = convert_distance(distance_kilometers, 'km', 'mi')
    print(f'{distance_kilometers} kilometers is {converted_mi} miles')
    converted_m = convert_distance(distance_miles, 'mi', 'm')
    print(f'{distance_miles} miles is {converted_m} meters')