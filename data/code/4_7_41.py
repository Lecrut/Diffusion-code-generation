class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371

    def convert(self, distance, from_unit, to_unit):
        if from_unit == 'miles' and to_unit == 'kilometers':
            return distance * self.MILES_TO_KILOMETERS
        elif from_unit == 'kilometers' and to_unit == 'miles':
            return distance * self.KILOMETERS_TO_MILES
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_distance_miles = 8.0
    sample_distance_kilometers = 13.0

    try:
        converted_to_km = converter.convert(sample_distance_miles, 'miles', 'kilometers')
        print(f"{sample_distance_miles} miles is {converted_to_km:.2f} kilometers")
    except ValueError as e:
        print(e)

    try:
        converted_to_miles = converter.convert(sample_distance_kilometers, 'kilometers', 'miles')
        print(f"{sample_distance_kilometers} kilometers is {converted_to_miles:.2f} miles")
    except ValueError as e:
        print(e)