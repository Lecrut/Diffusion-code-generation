class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            'mm': {'km': 1e-06, 'ft': 0.00328084, 'yd': 0.00109361},
            'km': {'mm': 1000000.0, 'ft': 3280.84, 'yd': 1093.61},
            'ft': {'mm': 304.8, 'km': 0.0003048, 'yd': 0.333333},
            'yd': {'mm': 914.4, 'km': 0.0009144, 'ft': 3.0}
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors[from_unit]:
            raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')
        return value * self.conversion_factors[from_unit][to_unit]

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1000, 'mm', 'km'))
    print(converter.convert(5, 'km', 'ft'))
    print(converter.convert(200, 'mm', 'yd'))
    print(converter.convert(10, 'yd', 'ft'))