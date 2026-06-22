class DistanceConverter:
    MILES = 0
    KILOMETERS = 1
    METERS = 2

    def __init__(self):
        self.FACTOR_MILES_TO_METERS = 1609.344
        self.FACTOR_KILOMETERS_TO_METERS = 1000.0
        self.FACTOR_METERS_TO_MILES = 1 / 1609.344
        self.FACTOR_METERS_TO_KILOMETERS = 1 / 1000.0
        self.FACTOR_KILOMETERS_TO_MILES = self.FACTOR_KILOMETERS_TO_METERS * self.FACTOR_METERS_TO_MILES
        self.FACTOR_MILES_TO_KILOMETERS = self.FACTOR_MILES_TO_METERS * self.FACTOR_METERS_TO_KILOMETERS

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == self.METERS:
            if to_unit == self.MILES:
                return value * self.FACTOR_METERS_TO_MILES
            return value * self.FACTOR_METERS_TO_KILOMETERS
        if from_unit == self.MILES:
            if to_unit == self.KILOMETERS:
                return value * self.FACTOR_MILES_TO_KILOMETERS
            return value * self.FACTOR_MILES_TO_METERS
        if from_unit == self.KILOMETERS:
            if to_unit == self.MILES:
                return value * self.FACTOR_KILOMETERS_TO_MILES
            return value * self.FACTOR_KILOMETERS_TO_METERS

if __name__ == '__main__':
    converter = DistanceConverter()
    result1 = converter.convert(5, DistanceConverter.MILES, DistanceConverter.KILOMETERS)
    result2 = converter.convert(1000, DistanceConverter.METERS, DistanceConverter.MILES)
    result3 = converter.convert(10, DistanceConverter.KILOMETERS, DistanceConverter.METERS)
    print(result1)
    print(result2)
    print(result3)