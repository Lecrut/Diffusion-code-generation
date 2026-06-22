class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371

    def convert(self, distance, unit_from, unit_to):
        if not isinstance(distance, (int, float)):
            raise ValueError('Distance must be a numeric value.')
        
        unit_from = unit_from.lower()
        unit_to = unit_to.lower()

        if unit_from == 'miles' and unit_to == 'kilometers':
            return distance * self.MILES_TO_KILOMETERS
        elif unit_from == 'kilometers' and unit_to == 'miles':
            return distance * self.KILOMETERS_TO_MILES
        else:
            raise ValueError("Unsupported conversion units. Use 'miles' or 'kilometers'.")

if __name__ == '__main__':
    converter = DistanceConverter()
    miles_distance = 5
    kilometers_distance = 8.0467

    print(f"{miles_distance} miles is {converter.convert(miles_distance, 'miles', 'kilometers')} kilometers")
    print(f"{kilometers_distance} kilometers is {converter.convert(kilometers_distance, 'kilometers', 'miles')} miles")