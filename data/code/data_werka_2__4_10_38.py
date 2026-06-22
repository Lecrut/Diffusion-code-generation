class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 1 / MILES_TO_KILOMETERS
    MILES_TO_METERS = 1609.34
    METERS_TO_MILES = 1 / MILES_TO_METERS
    KILOMETERS_TO_METERS = 1000
    METERS_TO_KILOMETERS = 1 / KILOMETERS_TO_METERS

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        conversion_factor = self._get_conversion_factor(from_unit, to_unit)
        return value * conversion_factor

    def _get_conversion_factor(self, from_unit, to_unit):
        if (from_unit, to_unit) == ('miles', 'kilometers'):
            return self.MILES_TO_KILOMETERS
        elif (from_unit, to_unit) == ('kilometers', 'miles'):
            return self.KILOMETERS_TO_MILES
        elif (from_unit, to_unit) == ('miles', 'meters'):
            return self.MILES_TO_METERS
        elif (from_unit, to_unit) == ('meters', 'miles'):
            return self.METERS_TO_MILES
        elif (from_unit, to_unit) == ('kilometers', 'meters'):
            return self.KILOMETERS_TO_METERS
        elif (from_unit, to_unit) == ('meters', 'kilometers'):
            return self.METERS_TO_KILOMETERS
        else:
            raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'meters'))
    print(converter.convert(2000, 'meters', 'miles'))