class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_METERS = 1000

    def __init__(self):
        self.valid_units = {'miles', 'kilometers', 'meters'}

    def _validate_conversion(self, from_unit, to_unit):
        if from_unit not in self.valid_units or to_unit not in self.valid_units:
            raise ValueError(f'Unsupported unit: {from_unit} or {to_unit}')

    def convert(self, value, from_unit, to_unit):
        self._validate_conversion(from_unit, to_unit)
        if from_unit == to_unit:
            return value
        intermediate_value = value
        if from_unit == 'miles':
            intermediate_value *= self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS
        elif from_unit == 'kilometers':
            intermediate_value *= self.KILOMETERS_TO_METERS
        if to_unit == 'miles':
            return intermediate_value / (self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS)
        elif to_unit == 'kilometers':
            return intermediate_value / self.KILOMETERS_TO_METERS
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'meters'))
    print(converter.convert(100, 'meters', 'miles'))