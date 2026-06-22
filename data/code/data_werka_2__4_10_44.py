class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_METERS = 1000

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        intermediate_value = self._convert_to_meters(value, from_unit)
        return self._convert_from_meters(intermediate_value, to_unit)

    def _convert_to_meters(self, value, unit):
        if unit == 'miles':
            return value * self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS
        elif unit == 'kilometers':
            return value * self.KILOMETERS_TO_METERS
        elif unit == 'meters':
            return value
        else:
            raise ValueError(f'Unsupported conversion from {unit} to meters')

    def _convert_from_meters(self, value, unit):
        if unit == 'miles':
            return value / (self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS)
        elif unit == 'kilometers':
            return value / self.KILOMETERS_TO_METERS
        elif unit == 'meters':
            return value
        else:
            raise ValueError(f'Unsupported conversion from meters to {unit}')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'meters'))
    print(converter.convert(100, 'meters', 'miles'))