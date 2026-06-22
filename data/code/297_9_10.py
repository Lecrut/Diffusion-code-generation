class DistanceConverter:
    MILE_TO_KILOMETER_FACTOR = 1.60934

    @staticmethod
    def miles_to_kilometers(miles):
        return miles * DistanceConverter.MILE_TO_KILOMETER_FACTOR

if __name__ == '__main__':
    sample_miles = 5
    result_km = DistanceConverter.miles_to_kilometers(sample_miles)
    print(result_km)