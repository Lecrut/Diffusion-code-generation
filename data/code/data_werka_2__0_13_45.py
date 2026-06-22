def convert_length(value, from_unit, to_unit):
    conversion_factors = {'m_to_cm': 100, 'cm_to_m': 0.01, 'm_to_in': 39.3701, 'in_to_m': 0.0254, 'cm_to_in': 0.393701, 'in_to_cm': 2.54}
    key = f'{from_unit}_to_{to_unit}'
    if key in conversion_factors:
        return value * conversion_factors[key]
    else:
        raise ValueError('Unsupported unit conversion')
if __name__ == '__main__':
    print(convert_length(1, 'm', 'cm'))
    print(convert_length(2.54, 'cm', 'in'))
    print(convert_length(39.3701, 'in', 'm'))