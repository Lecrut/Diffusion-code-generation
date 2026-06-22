class DistanceConverter:
    MILES_TO_FEET_FACTOR = 5280

    @staticmethod
    def miles_to_feet(miles):
        return miles * DistanceConverter.MILES_TO_FEET_FACTOR

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_miles = 10.5
    result = DistanceConverter.miles_to_feet(sample_miles)
    print(result)