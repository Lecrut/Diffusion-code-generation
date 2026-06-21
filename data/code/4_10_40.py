class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_METERS = 1000

    def __init__(self):
        self.conversion_factors = {
            'miles_to_kilometers': self.MILES_TO_KILOMETERS,
            'kilometers_to_meters': self.KILOMETERS_TO_METERS,
            'miles_to_meters': self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS,
            'kilometers_to_miles': 1 / self.MILES_TO_KILOMETERS,
            'meters_to_kilometers': 1 / self.KILOMETERS_TO_METERS,
            'meters_to_miles': 1 / (self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS)
        }

    def validate_units(self, from_unit, to_unit):
        valid_units = ['miles', 'kilometers', 'meters']
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f'Invalid unit(s): {from_unit} and/or {to_unit}')

    def convert(self, value, from_unit, to_unit):
        self.validate_units(from_unit, to_unit)
        if from_unit == to_unit:
            return value
        conversion_key = f'{from_unit}_to_{to_unit}'
        if conversion_key in self.conversion_factors:
            return value * self.conversion_factors[conversion_key]
        else:
            raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'meters'))
    print(converter.convert(100, 'meters', 'miles'))