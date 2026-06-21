class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371

    def __init__(self):
        self.conversion_factors = {
            ('miles', 'kilometers'): DistanceConverter.MILES_TO_KILOMETERS,
            ('kilometers', 'miles'): DistanceConverter.KILOMETERS_TO_MILES
        }

    def convert(self, distance, unit_from, unit_to):
        if not isinstance(distance, (int, float)):
            raise ValueError('Distance must be a numeric value.')
        
        unit_from = unit_from.lower()
        unit_to = unit_to.lower()

        conversion_key = (unit_from, unit_to)
        if conversion_key in self.conversion_factors:
            return distance * self.conversion_factors[conversion_key]
        else:
            raise ValueError("Unsupported conversion units. Use 'miles' or 'kilometers'.")

if __name__ == '__main__':
    converter = DistanceConverter()
    miles_distance = 15
    kilometers_distance = converter.convert(miles_distance, 'miles', 'kilometers')
    print(f"{miles_distance} miles is {kilometers_distance} kilometers")

    kilometers_distance = 25.8032
    miles_distance = converter.convert(kilometers_distance, 'kilometers', 'miles')
    print(f"{kilometers_distance} kilometers is {miles_distance} miles")