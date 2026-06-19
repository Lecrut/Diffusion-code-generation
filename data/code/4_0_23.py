def convert_distance(value, from_unit, to_unit):
    conversion_factors = {'m_to_km': 0.001, 'km_to_m': 1000, 'm_to_mi': 0.000621371, 'mi_to_m': 1609.34, 'km_to_mi': 0.621371, 'mi_to_km': 1.60934}
    valid_units = ['m', 'km', 'mi']
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("Invalid unit. Please use 'm' for meters, 'km' for kilometers, or 'mi' for miles.")
    if from_unit == to_unit:
        return value
    conversion_key = f'{from_unit}_to_{to_unit}'
    if conversion_key not in conversion_factors:
        raise ValueError('Conversion between these units is not supported.')
    converted_value = value * conversion_factors[conversion_key]
    return converted_value
if __name__ == '__main__':
    distance_meters = 1000
    distance_kilometers = 5
    distance_miles = 3
    print('1000 meters to kilometers:', convert_distance(distance_meters, 'm', 'km'))
    print('5 kilometers to miles:', convert_distance(distance_kilometers, 'km', 'mi'))
    print('3 miles to meters:', convert_distance(distance_miles, 'mi', 'm'))