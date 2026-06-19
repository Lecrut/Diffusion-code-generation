def convert_distance(value, from_unit, to_unit):
    conversion_factors = {'m_to_km': 0.001, 'km_to_m': 1000, 'm_to_mi': 0.000621371, 'mi_to_m': 1609.34, 'km_to_mi': 0.621371, 'mi_to_km': 1.60934}
    valid_units = ['m', 'km', 'mi']
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("Invalid unit. Please use 'm' for meters, 'km' for kilometers, or 'mi' for miles.")
    if from_unit == to_unit:
        return value
    elif from_unit == 'm':
        if to_unit == 'km':
            conversion_key = 'm_to_km'
        else:
            conversion_key = 'm_to_mi'
    elif from_unit == 'km':
        if to_unit == 'm':
            conversion_key = 'km_to_m'
        else:
            conversion_key = 'km_to_mi'
    elif to_unit == 'm':
        conversion_key = 'mi_to_m'
    else:
        conversion_key = 'mi_to_km'
    return value * conversion_factors[conversion_key]
if __name__ == '__main__':
    print(convert_distance(1000, 'm', 'km'))
    print(convert_distance(5, 'km', 'mi'))
    print(convert_distance(10, 'mi', 'm'))
    print(convert_distance(2.5, 'km', 'km'))