class LengthConverter:

    def __init__(self):
        self.conversions = {'m': 1, 'pm': 1e-12}

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.conversions or to_unit not in self.conversions:
            raise ValueError('Invalid unit specified')
        meters = value * self.conversions[from_unit]
        return meters / self.conversions[to_unit]
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1, 'pm', 'm'))
    print(converter.convert(1000000, 'pm', 'm'))