class DistanceConverter:
    MILES_TO_KILOMETERS = 1.609344
    MILES_TO_METERS = 1609.344
    KILOMETERS_TO_MILES = 1 / 1.609344
    KILOMETERS_TO_METERS = 1000.0
    METERS_TO_MILES = 1 / 1609.344
    METERS_TO_KILOMETERS = 1 / 1000.0

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        if from_unit == 'miles':
            if to_unit == 'kilometers':
                return value * self.MILES_TO_KILOMETERS
            if to_unit == 'meters':
                return value * self.MILES_TO_METERS

        if from_unit == 'kilometers':
            if to_unit == 'miles':
                return value * self.KILOMETERS_TO_MILES
            if to_unit == 'meters':
                return value * self.KILOMETERS_TO_METERS

        if from_unit == 'meters':
            if to_unit == 'miles':
                return value * self.METERS_TO_MILES
            if to_unit == 'kilometers':
                return value * self.METERS_TO_KILOMETERS

        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.convert(5, 'miles', 'kilometers')
    print(result)
    result2 = converter.convert(1000, 'meters', 'miles')
    print(result2)
    result3 = converter.convert(2, 'kilometers', 'meters')
    print(result3)