def convert_length(value, from_unit, to_unit):
    conversion_factors = {'m': {'cm': 100, 'in': 39.3701}, 'cm': {'m': 0.01, 'in': 0.393701}, 'in': {'m': 0.0254, 'cm': 2.54}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError('Unsupported unit conversion')
    return value * conversion_factors[from_unit][to_unit]
if __name__ == '__main__':
    print(convert_length(1, 'm', 'cm'))
    print(convert_length(2.54, 'cm', 'in'))
    print(convert_length(39.3701, 'in', 'm'))