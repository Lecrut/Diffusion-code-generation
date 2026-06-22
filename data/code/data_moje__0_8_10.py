class LengthConverter:
    METERS_TO_FEET = 3.28084
    FEET_TO_METERS = 0.3048

    VALID_UNITS = {'meters', 'feet'}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.VALID_UNITS or to_unit not in self.VALID_UNITS:
            raise ValueError("Unsupported unit. Use 'meters' or 'feet'.")

        if from_unit == to_unit:
            return value

        if from_unit == 'meters' and to_unit == 'feet':
            return value * self.METERS_TO_FEET
        elif from_unit == 'feet' and to_unit == 'meters':
            return value * self.FEET_TO_METERS
        else:
            raise ValueError("Conversion not supported.")

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1.0, 'meters', 'feet'))
    print(converter.convert(3.28084, 'feet', 'meters'))
    print(converter.convert(100, 'meters', 'feet'))
    print(converter.convert(50, 'feet', 'meters'))