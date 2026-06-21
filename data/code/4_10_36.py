class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_METERS = 1000

    def __init__(self):
        self.conversion_map = {('miles', 'kilometers'): self.MILES_TO_KILOMETERS, ('kilometers', 'meters'): self.KILOMETERS_TO_METERS, ('miles', 'meters'): self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS, ('kilometers', 'miles'): 1 / self.MILES_TO_KILOMETERS, ('meters', 'kilometers'): 1 / self.KILOMETERS_TO_METERS, ('meters', 'miles'): 1 / (self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS)}

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        conversion_key = (from_unit, to_unit)
        if conversion_key in self.conversion_map:
            return value * self.conversion_map[conversion_key]
        else:
            raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'meters'))
    print(converter.convert(100, 'meters', 'miles'))