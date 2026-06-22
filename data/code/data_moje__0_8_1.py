class LengthConverter:
    METERS_PER_FOOT = 0.3048

    def convert(self, value, from_unit, to_unit):
        if from_unit.lower() == to_unit.lower():
            return value
        if from_unit.lower() == 'meters' and to_unit.lower() == 'feet':
            return value / self.METERS_PER_FOOT
        if from_unit.lower() == 'feet' and to_unit.lower() == 'meters':
            return value * self.METERS_PER_FOOT
        raise ValueError(f"Unsupported units: {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1, 'meters', 'feet'))
    print(converter.convert(1, 'feet', 'meters'))