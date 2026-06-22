def convert_length(value, from_unit, to_unit):
    conversion_factors = {'mm_to_km': 1e-06, 'km_to_mm': 1000000.0, 'mm_to_m': 0.001, 'm_to_mm': 1000, 'mm_to_cm': 0.1, 'cm_to_mm': 10, 'mm_to_in': 0.0393701, 'in_to_mm': 25.4, 'mm_to_ft': 0.00328084, 'ft_to_mm': 304.8, 'mm_to_yd': 0.00109361, 'yd_to_mm': 914.4, 'km_to_m': 1000, 'm_to_km': 0.001, 'km_to_ft': 3280.84, 'ft_to_km': 0.0003048, 'km_to_yd': 1093.61, 'yd_to_km': 0.0009144, 'm_to_ft': 3.28084, 'ft_to_m': 0.3048, 'm_to_yd': 1.09361, 'yd_to_m': 0.9144, 'in_to_cm': 2.54, 'cm_to_in': 0.393701}
    conversion_key = f'{from_unit}_to_{to_unit}'
    if conversion_key not in conversion_factors:
        raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')
    return value * conversion_factors[conversion_key]
if __name__ == '__main__':
    print(convert_length(1000, 'mm', 'km'))
    print(convert_length(5, 'km', 'm'))
    print(convert_length(10, 'ft', 'yd'))
    print(convert_length(2, 'yd', 'in'))