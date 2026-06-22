class DistanceConverter:
    def __init__(self):
        self._units = {'meters', 'kilometers', 'miles'}
        self._conversion_factors = {
            'meters': 1.0,
            'kilometers': 1000.0,
            'miles': 1609.344
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self._units or to_unit not in self._units:
            raise ValueError("Invalid unit. Supported units: meters, kilometers, miles")
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise ValueError("Distance cannot be negative")
        meters = value * self._conversion_factors[from_unit]
        result = meters / self._conversion_factors[to_unit]
        return round(result, 6)

    def meters_to_kilometers(self, meters):
        return self.convert(meters, 'meters', 'kilometers')

    def meters_to_miles(self, meters):
        return self.convert(meters, 'meters', 'miles')

    def kilometers_to_meters(self, kilometers):
        return self.convert(kilometers, 'kilometers', 'meters')

    def kilometers_to_miles(self, kilometers):
        return self.convert(kilometers, 'kilometers', 'miles')

    def miles_to_meters(self, miles):
        return self.convert(miles, 'miles', 'meters')

    def miles_to_kilometers(self, miles):
        return self.convert(miles, 'miles', 'kilometers')

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.meters_to_kilometers(1000))
    print(converter.kilometers_to_miles(5))
    print(converter.miles_to_meters(1))
    print(converter.convert(1609.344, 'meters', 'miles'))