def convert_distance(value, from_unit, to_unit):
    conversion_factors = {'m_to_km': 0.001, 'km_to_m': 1000, 'm_to_mi': 0.000621371, 'mi_to_m': 1609.34, 'km_to_mi': 0.621371, 'mi_to_km': 1.60934}
    valid_units = ['m', 'km', 'mi']
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("Invalid unit. Please use 'm' for meters, 'km' for kilometers, or 'mi' for miles.")
    if from_unit == 'm' and to_unit == 'km':
        conversion_key = 'm_to_km'
    elif from_unit == 'km' and to_unit == 'm':
        conversion_key = 'km_to_m'
    elif from_unit == 'm' and to_unit == 'mi':
        conversion_key = 'm_to_mi'
    elif from_unit == 'mi' and to_unit == 'm':
        conversion_key = 'mi_to_m'
    elif from_unit == 'km' and to_unit == 'mi':
        conversion_key = 'km_to_mi'
    elif from_unit == 'mi' and to_unit == 'km':
        conversion_key = 'mi_to_km'
    converted_value = value * conversion_factors[conversion_key]
    return converted_value
if __name__ == '__main__':
    sample_values = [(100, 'm', 'km'), (5, 'km', 'm'), (2, 'mi', 'km'), (3.1, 'km', 'mi')]
    for value, from_unit, to_unit in sample_values:
        result = convert_distance(value, from_unit, to_unit)
        print(f'{value} {from_unit} is equal to {result:.4f} {to_unit}')