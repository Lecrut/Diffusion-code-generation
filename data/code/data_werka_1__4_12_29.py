class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 1 / MILES_TO_KILOMETERS
    METERS_TO_KILOMETERS = 0.001
    KILOMETERS_TO_METERS = 1 / METERS_TO_KILOMETERS
    MILES_TO_METERS = MILES_TO_KILOMETERS * METERS_TO_KILOMETERS

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'miles':
            if to_unit == 'kilometers':
                return value * self.MILES_TO_KILOMETERS
            elif to_unit == 'meters':
                return value * self.MILES_TO_METERS
        elif from_unit == 'kilometers':
            if to_unit == 'miles':
                return value * self.KILOMETERS_TO_MILES
            elif to_unit == 'meters':
                return value * self.KILOMETERS_TO_METERS
        elif from_unit == 'meters':
            if to_unit == 'miles':
                return value / self.MILES_TO_METERS
            elif to_unit == 'kilometers':
                return value * self.METERS_TO_KILOMETERS
        raise ValueError('Unsupported conversion')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'meters'))
    print(converter.convert(2000, 'meters', 'miles'))