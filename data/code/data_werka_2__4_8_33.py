class DistanceConverter:

    def __init__(self):
        self.miles_to_kilometers = 1.60934
        self.kilometers_to_miles = 0.621371

    def convert(self, distance, unit_from, unit_to):
        if not isinstance(distance, (int, float)):
            raise ValueError('Distance must be a numeric value.')
        if unit_from.lower() == 'miles' and unit_to.lower() == 'kilometers':
            return distance * self.miles_to_kilometers
        elif unit_from.lower() == 'kilometers' and unit_to.lower() == 'miles':
            return distance * self.kilometers_to_miles
        else:
            raise ValueError("Unsupported conversion units. Use 'miles' or 'kilometers'.")
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(10, 'miles', 'kilometers'))
    print(converter.convert(16.0934, 'kilometers', 'miles'))