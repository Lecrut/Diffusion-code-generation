class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_METERS = 1000

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        intermediate_value = self._convert_to_meters(value, from_unit)
        return self._convert_from_meters(intermediate_value, to_unit)

    def _convert_to_meters(self, value, from_unit):
        if from_unit == 'miles':
            return value * self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS
        elif from_unit == 'kilometers':
            return value * self.KILOMETERS_TO_METERS
        elif from_unit == 'meters':
            return value
        else:
            raise ValueError(f'Unsupported conversion from {from_unit} to meters')

    def _convert_from_meters(self, value, to_unit):
        if to_unit == 'miles':
            return value / (self.MILES_TO_KILOMETERS * self.KILOMETERS_TO_METERS)
        elif to_unit == 'kilometers':
            return value / self.KILOMETERS_TO_METERS
        elif to_unit == 'meters':
            return value
        else:
            raise ValueError(f'Unsupported conversion to {to_unit}')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'meters'))
    print(converter.convert(100, 'meters', 'miles'))