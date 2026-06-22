class LengthConverter:

    def __init__(self):
        self.units = {'in': 2.54, 'cm': 1, 'm': 100, 'km': 100000}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError('Invalid unit')
        return value * self.units[from_unit] / self.units[to_unit]
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'cm', 'in'))