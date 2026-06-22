def convert_length(value, from_unit, to_unit):
    conversion_factors = {'mm_to_km': 1e-06, 'km_to_mm': 1000000.0, 'mm_to_ft': 0.00328084, 'ft_to_mm': 304.8, 'mm_to_yd': 0.00109361, 'yd_to_mm': 914.4, 'km_to_ft': 3280.84, 'ft_to_km': 0.0003048, 'km_to_yd': 1093.61, 'yd_to_km': 0.0009144, 'ft_to_yd': 0.333333, 'yd_to_ft': 3.0}
    conversion_key = f'{from_unit}_to_{to_unit}'
    if conversion_key not in conversion_factors:
        raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
    return value * conversion_factors[conversion_key]
if __name__ == '__main__':
    print(convert_length(1000, 'mm', 'km'))
    print(convert_length(1, 'km', 'ft'))
    print(convert_length(500, 'mm', 'yd'))
    print(convert_length(10, 'yd', 'ft'))