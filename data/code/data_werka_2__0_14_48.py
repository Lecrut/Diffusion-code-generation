def convert_length(value, from_unit, to_unit):
    conversion_factors = {'mm': 1, 'km': 1000000, 'ft': 304.8, 'yd': 914.4}
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError('Unsupported unit')
    value_in_mm = value * conversion_factors[from_unit]
    converted_value = value_in_mm / conversion_factors[to_unit]
    return converted_value
if __name__ == '__main__':
    sample_values = [(1000, 'mm', 'km'), (5, 'yd', 'ft'), (1, 'km', 'mm'), (12, 'ft', 'yd')]
    for value, from_unit, to_unit in sample_values:
        result = convert_length(value, from_unit, to_unit)
        print(f'{value} {from_unit} is {result:.6f} {to_unit}')