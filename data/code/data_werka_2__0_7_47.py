class LengthConverter:

    def __init__(self):
        self.supported_units = {'m', 'ft'}

    def validate_units(self, from_unit, to_unit):
        if from_unit not in self.supported_units or to_unit not in self.supported_units:
            raise ValueError('Unsupported unit conversion')

    def convert(self, value, from_unit, to_unit):
        self.validate_units(from_unit, to_unit)
        if from_unit == 'm' and to_unit == 'ft':
            return value * 3.28084
        elif from_unit == 'ft' and to_unit == 'm':
            return value / 3.28084
        else:
            raise ValueError('Unsupported unit conversion')
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'm', 'ft'))
    print(converter.convert(50, 'ft', 'm'))