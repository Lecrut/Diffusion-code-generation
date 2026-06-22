class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371

    @staticmethod
    def convert(distance, from_unit, to_unit):
        if (from_unit == 'miles' and to_unit == 'kilometers'):
            return distance * DistanceConverter.MILES_TO_KILOMETERS
        elif (from_unit == 'kilometers' and to_unit == 'miles'):
            return distance * DistanceConverter.KILOMETERS_TO_MILES
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    sample_distance_miles = 8.0
    sample_distance_kilometers = 13.0

    converted_to_km = DistanceConverter.convert(sample_distance_miles, 'miles', 'kilometers')
    print(f"{sample_distance_miles} miles is {converted_to_km:.2f} kilometers")

    converted_to_miles = DistanceConverter.convert(sample_distance_kilometers, 'kilometers', 'miles')
    print(f"{sample_distance_kilometers} kilometers is {converted_to_miles:.2f} miles")