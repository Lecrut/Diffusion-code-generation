class DistanceConverter:
    CONVERSION_FACTORS = {('miles', 'kilometers'): 1.60934, ('kilometers', 'meters'): 1000, ('miles', 'meters'): 1.60934 * 1000, ('kilometers', 'miles'): 1 / 1.60934, ('meters', 'kilometers'): 1 / 1000, ('meters', 'miles'): 1 / (1.60934 * 1000)}

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        conversion_key = (from_unit, to_unit)
        if conversion_key in self.CONVERSION_FACTORS:
            return value * self.CONVERSION_FACTORS[conversion_key]
        else:
            raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'meters'))
    print(converter.convert(100, 'meters', 'miles'))