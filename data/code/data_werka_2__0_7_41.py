class LengthConverter:

    def __init__(self):
        self.conversion_map = {'m': {'ft': 3.28084}, 'ft': {'m': 1 / 3.28084}}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_map or to_unit not in self.conversion_map[from_unit]:
            raise ValueError('Unsupported unit conversion')
        return value * self.conversion_map[from_unit][to_unit]
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(5, 'm', 'ft'))
    print(converter.convert(16.4042, 'ft', 'm'))