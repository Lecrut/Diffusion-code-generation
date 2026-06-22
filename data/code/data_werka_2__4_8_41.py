class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371

    def __init__(self):
        self.supported_units = {'miles', 'kilometers'}

    def _validate_distance(self, distance):
        if not isinstance(distance, (int, float)):
            raise ValueError('Distance must be a numeric value.')

    def _validate_units(self, unit_from, unit_to):
        if unit_from.lower() not in self.supported_units or unit_to.lower() not in self.supported_units:
            raise ValueError("Unsupported conversion units. Use 'miles' or 'kilometers'.")

    def convert(self, distance, unit_from, unit_to):
        self._validate_distance(distance)
        self._validate_units(unit_from, unit_to)

        if unit_from.lower() == 'miles' and unit_to.lower() == 'kilometers':
            return distance * self.MILES_TO_KILOMETERS
        elif unit_from.lower() == 'kilometers' and unit_to.lower() == 'miles':
            return distance * self.KILOMETERS_TO_MILES

if __name__ == '__main__':
    converter = DistanceConverter()
    miles_distance = 10
    kilometers_distance = 16.0934
    print(f"{miles_distance} miles is {converter.convert(miles_distance, 'miles', 'kilometers')} kilometers")
    print(f"{kilometers_distance} kilometers is {converter.convert(kilometers_distance, 'kilometers', 'miles')} miles")