from typing import Union

def convert_volume(value: float, from_unit: str, to_unit: str) -> float:
    conversion_factors = {'L_to_mL': 1000, 'mL_to_L': 0.001, 'm3_to_L': 1000, 'L_to_m3': 0.001, 'L_to_gal': 0.264172, 'gal_to_L': 3.78541}
    valid_units = ['L', 'mL', 'm³', 'gal']
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError('Invalid unit provided')
    direct_conversion_key = f'{from_unit}_to_{to_unit}'
    reverse_conversion_key = f'{to_unit}_to_{from_unit}'
    if direct_conversion_key in conversion_factors:
        return value * conversion_factors[direct_conversion_key]
    elif reverse_conversion_key in conversion_factors:
        return value / conversion_factors[reverse_conversion_key]
    else:
        raise ValueError('Conversion between these units is not supported')
if __name__ == '__main__':
    print(convert_volume(10, 'L', 'mL'))
    print(convert_volume(500, 'mL', 'L'))
    print(convert_volume(2, 'm³', 'L'))
    print(convert_volume(1, 'L', 'gal'))
    print(convert_volume(1, 'gal', 'L'))