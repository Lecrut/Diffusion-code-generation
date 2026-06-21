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
        if from_unit == 'miles' and to_unit == 'kilometers':
            return value * self.MILES_TO_KILOMETERS
        elif from_unit == 'kilometers' and to_unit == 'miles':
            return value * self.KILOMETERS_TO_MILES
        elif from_unit == 'miles' and to_unit == 'meters':
            return value * self.MILES_TO_METERS
        elif from_unit == 'meters' and to_unit == 'miles':
            return value * self.METERS_TO_MILES
        elif from_unit == 'kilometers' and to_unit == 'meters':
            return value * self.KILOMETERS_TO_METERS
        elif from_unit == 'meters' and to_unit == 'kilometers':
            return value * self.METERS_TO_KILOMETERS
        else:
            raise ValueError('Unsupported conversion')
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(5, 'kilometers', 'miles'))
    print(converter.convert(100, 'miles', 'meters'))
    print(converter.convert(2000, 'meters', 'kilometers'))