class DistanceConverter:
    CONVERSION_FACTOR = 1.852

    @staticmethod
    def nautical_miles_to_kilometers(nautical_miles):
        if nautical_miles == 0:
            return 0
        return nautical_miles * DistanceConverter.CONVERSION_FACTOR

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.nautical_miles_to_kilometers(0))
    print(converter.nautical_miles_to_kilometers(1))
    print(converter.nautical_miles_to_kilometers(10))
    print(converter.nautical_miles_to_kilometers(100))