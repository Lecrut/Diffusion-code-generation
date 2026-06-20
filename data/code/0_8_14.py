class LengthConverter:
    METERS_PER_FOOT = 0.3048

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'meters' and to_unit == 'feet':
            return value / self.METERS_PER_FOOT
        if from_unit == 'feet' and to_unit == 'meters':
            return value * self.METERS_PER_FOOT
        raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1, 'meters', 'feet'))
    print(converter.convert(3.28084, 'feet', 'meters'))
    print(converter.convert(100, 'feet', 'meters'))
    print(converter.convert(30.48, 'meters', 'feet'))