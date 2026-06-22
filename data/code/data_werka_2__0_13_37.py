def convert_length(value, from_unit, to_unit):
    conversion_factors = {'m_to_cm': 100, 'cm_to_m': 0.01, 'm_to_in': 39.3701, 'in_to_m': 0.0254, 'cm_to_in': 0.393701, 'in_to_cm': 2.54}
    key = f'{from_unit}_to_{to_unit}'
    if key not in conversion_factors:
        raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
    return value * conversion_factors[key]
if __name__ == '__main__':
    print(convert_length(1, 'm', 'cm'))
    print(convert_length(100, 'cm', 'm'))
    print(convert_length(2.54, 'cm', 'in'))
    print(convert_length(1, 'm', 'in'))
    print(convert_length(39.3701, 'in', 'm'))