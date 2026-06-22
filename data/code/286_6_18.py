class LengthConverter:

    def __init__(self):
        self.conversion_factors = {'in': 0.0254, 'cm': 0.01, 'm': 1, 'km': 1000}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError('Invalid unit')
        return value * self.conversion_factors[from_unit] / self.conversion_factors[to_unit]
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'in', 'cm'))
    print(converter.convert(5, 'cm', 'm'))
    try:
        print(converter.convert(2, 'ft', 'mi'))
    except ValueError as e:
        print(e)