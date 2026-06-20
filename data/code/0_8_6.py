class LengthConverter:
    def __init__(self):
        self.conversion_factors = {
            ('meters', 'feet'): 3.28084,
            ('feet', 'meters'): 0.3048
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        factor = self.conversion_factors.get((from_unit, to_unit))
        if factor is None:
            raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
        return value * factor

if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.convert(1, 'meters', 'feet'))
    print(converter.convert(3.28084, 'feet', 'meters'))