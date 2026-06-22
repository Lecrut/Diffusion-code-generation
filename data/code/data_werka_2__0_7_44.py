class LengthConverter:

    def __init__(self):
        self.conversion_table = {'m': {'ft': 3.28084}, 'ft': {'m': 1 / 3.28084}}

    def convert(self, value, from_unit, to_unit):
        if from_unit in self.conversion_table and to_unit in self.conversion_table[from_unit]:
            return value * self.conversion_table[from_unit][to_unit]
        else:
            raise ValueError('Unsupported unit conversion')
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'm', 'ft'))
    print(converter.convert(32.8084, 'ft', 'm'))