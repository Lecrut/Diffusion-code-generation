class DistanceConverter:
    conversion_factor = 1.852

    @staticmethod
    def nautical_miles_to_kilometers(nautical_miles):
        if nautical_miles == 0:
            return 0
        return nautical_miles * DistanceConverter.conversion_factor

if __name__ == '__main__':
    converter = DistanceConverter()
    print(f"0 nautical miles is {converter.nautical_miles_to_kilometers(0)} kilometers")
    print(f"1 nautical mile is {converter.nautical_miles_to_kilometers(1)} kilometers")
    print(f"5 nautical miles is {converter.nautical_miles_to_kilometers(5)} kilometers")
    print(f"100 nautical miles is {converter.nautical_miles_to_kilometers(100)} kilometers")