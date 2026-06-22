class UnitConverter:
    def __init__(self, from_unit, to_unit):
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.conversion_factors = {
            ('miles', 'feet'): 5280,
            ('feet', 'miles'): 1 / 5280,
            ('meters', 'feet'): 3.28084,
            ('feet', 'meters'): 1 / 3.28084,
            ('kilometers', 'miles'): 0.621371,
            ('miles', 'kilometers'): 1 / 0.621371,
        }

    def convert(self, value):
        key = (self.from_unit, self.to_unit)
        if key not in self.conversion_factors:
            raise ValueError(f"Conversion from {self.from_unit} to {self.to_unit} is not supported.")
        factor = self.conversion_factors[key]
        return value * factor

if __name__ == '__main__':
    converter = UnitConverter('miles', 'feet')
    result = converter.convert(5)
    print(result)