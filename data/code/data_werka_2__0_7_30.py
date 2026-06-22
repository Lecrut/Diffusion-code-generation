class LengthConverter:

    def convert(self, value, from_unit, to_unit):
        if from_unit == 'meters' and to_unit == 'feet':
            return value * 3.28084
        elif from_unit == 'feet' and to_unit == 'meters':
            return value / 3.28084
        else:
            raise ValueError('Unsupported unit conversion')
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(10, 'meters', 'feet'))
    print(converter.convert(32.8084, 'feet', 'meters'))