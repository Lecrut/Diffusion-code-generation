def convert_length(value, from_unit, to_unit):
    conversion_factors = {'mm': {'km': 1e-06, 'm': 0.001, 'cm': 0.1, 'in': 0.0393701, 'ft': 0.00328084, 'yd': 0.00109361}, 'km': {'mm': 1000000.0, 'm': 1000, 'cm': 100000, 'in': 39370.1, 'ft': 3280.84, 'yd': 1093.61}, 'm': {'mm': 1000, 'km': 0.001, 'cm': 100, 'in': 39.3701, 'ft': 3.28084, 'yd': 1.09361}, 'cm': {'mm': 10, 'km': 1e-05, 'm': 0.01, 'in': 0.393701, 'ft': 0.0328084, 'yd': 0.0109361}, 'in': {'mm': 25.4, 'km': 2.54e-05, 'm': 0.0254, 'cm': 2.54, 'ft': 0.0833333, 'yd': 0.0277778}, 'ft': {'mm': 304.8, 'km': 0.0003048, 'm': 0.3048, 'cm': 30.48, 'in': 12, 'yd': 0.333333}, 'yd': {'mm': 914.4, 'km': 0.0009144, 'm': 0.9144, 'cm': 91.44, 'in': 36, 'ft': 3}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        raise ValueError('Unsupported unit conversion')
    return value * conversion_factors[from_unit][to_unit]
if __name__ == '__main__':
    print(convert_length(1000, 'mm', 'km'))
    print(convert_length(5, 'km', 'm'))
    print(convert_length(12, 'in', 'ft'))
    print(convert_length(3, 'yd', 'cm'))