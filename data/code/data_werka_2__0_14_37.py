def convert_length(value, from_unit, to_unit):
    conversion_factors = {'mm_to_km': 1e-06, 'km_to_mm': 1000000.0, 'mm_to_ft': 3.28084 * 0.001, 'ft_to_mm': 1 / (3.28084 * 0.001), 'mm_to_yd': 1.09361 * 0.001, 'yd_to_mm': 1 / (1.09361 * 0.001), 'km_to_ft': 3280.84, 'ft_to_km': 1 / 3280.84, 'km_to_yd': 1093.61, 'yd_to_km': 1 / 1093.61, 'ft_to_yd': 3, 'yd_to_ft': 1 / 3}
    conversion_key = f'{from_unit}_to_{to_unit}'
    if conversion_key not in conversion_factors:
        raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')
    return value * conversion_factors[conversion_key]
if __name__ == '__main__':
    print(convert_length(1000, 'mm', 'km'))
    print(convert_length(5, 'km', 'ft'))
    print(convert_length(20, 'yd', 'mm'))
    print(convert_length(100, 'ft', 'yd'))