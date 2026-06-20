class DistanceConverter:
    MILES_PER_KILOMETER = 0.621371192237
    KILOMETERS_PER_MILE = 1.609344

    def __init__(self):
        self.miles_to_km = self.KILOMETERS_PER_MILE
        self.km_to_miles = self.MILES_PER_KILOMETER

    def _verify_numeric(self, value):
        if isinstance(value, bool):
            raise TypeError("Boolean values are not accepted as distance")
        if not isinstance(value, (int, float)):
            raise TypeError("Distance value must be a number")
        if value < 0:
            raise ValueError("Distance cannot be negative")
        return value

    def convert_miles_to_kilometers(self, miles):
        valid_miles = self._verify_numeric(miles)
        return valid_miles * self.miles_to_km

    def convert_kilometers_to_miles(self, kilometers):
        valid_km = self._verify_numeric(kilometers)
        return valid_km * self.km_to_miles

if __name__ == '__main__':
    converter = DistanceConverter()
    result_kilometers = converter.convert_miles_to_kilometers(5)
    result_miles = converter.convert_kilometers_to_miles(10)
    print(result_kilometers)
    print(result_miles)
    try:
        converter.convert_miles_to_kilometers("ten")
    except TypeError as error:
        print(error)
    try:
        converter.convert_kilometers_to_miles(-5)
    except ValueError as error:
        print(error)