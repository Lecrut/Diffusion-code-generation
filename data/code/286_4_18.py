class MeasurementConverter:

    def __init__(self):
        self.conversion_factors = {'mm': 0.0393701, 'in': 1}

    def convert(self, value, unit_from='mm', unit_to='in'):
        if unit_from not in self.conversion_factors or unit_to not in self.conversion_factors:
            raise ValueError('Invalid unit')
        return value * (self.conversion_factors[unit_from] / self.conversion_factors[unit_to])
if __name__ == '__main__':
    converter = MeasurementConverter()
    print(converter.convert(100, 'mm', 'in'))
    print(converter.convert(5, 'in', 'mm'))