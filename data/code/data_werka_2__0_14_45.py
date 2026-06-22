def convert_length(value, from_unit, to_unit):
    conversion_factors = {'mm': {'km': 1e-06, 'ft': 0.00328084, 'yd': 0.00109361}, 'km': {'mm': 1000000.0, 'ft': 3280.84, 'yd': 1093.61}, 'ft': {'mm': 304.8, 'km': 0.000328084, 'yd': 0.333333}, 'yd': {'mm': 914.4, 'km': 0.00109361, 'ft': 3}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError('Unsupported unit conversion')
    return value * conversion_factors[from_unit][to_unit]
if __name__ == '__main__':
    print(convert_length(1000, 'mm', 'km'))
    print(convert_length(1, 'km', 'ft'))
    print(convert_length(5280, 'ft', 'yd'))
    print(convert_length(360, 'yd', 'mm'))