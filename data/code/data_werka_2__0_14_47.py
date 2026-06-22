def convert_length(value, from_unit, to_unit):
    conversion_factors = {'mm': 1, 'km': 1000000, 'ft': 304.8, 'yd': 914.4}
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError('Unsupported unit')
    value_in_mm = value * conversion_factors[from_unit]
    converted_value = value_in_mm / conversion_factors[to_unit]
    return converted_value
if __name__ == '__main__':
    print(convert_length(1000, 'mm', 'km'))
    print(convert_length(5, 'yd', 'ft'))
    print(convert_length(10, 'km', 'mm'))
    print(convert_length(20, 'ft', 'yd'))