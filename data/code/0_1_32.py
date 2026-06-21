class UnitConverter:
    CONVERSION_FACTORS = {('meters', 'feet'): 3.28084, ('feet', 'meters'): 1 / 3.28084, ('meters', 'kilometers'): 0.001, ('kilometers', 'meters'): 1000}

    def convert(self, value, from_unit, to_unit):
        key = (from_unit.lower(), to_unit.lower())
        if key in self.CONVERSION_FACTORS:
            return value * self.CONVERSION_FACTORS[key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} is not supported.')
if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.convert(10, 'meters', 'feet'))
    print(converter.convert(32.8084, 'feet', 'meters'))
    print(converter.convert(5000, 'meters', 'kilometers'))