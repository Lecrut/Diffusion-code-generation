class LengthConverter:

    def convert(self, value, from_unit, to_unit):
        if from_unit == 'm' and to_unit == 'ft':
            return value * 3.28084
        elif from_unit == 'ft' and to_unit == 'm':
            return value / 3.28084
        else:
            raise ValueError('Unsupported conversion units')
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'm', 'ft'))
    print(converter.convert(32.8084, 'ft', 'm'))