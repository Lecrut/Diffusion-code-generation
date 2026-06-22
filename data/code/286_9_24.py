class DistanceConverter:
    def __init__(self):
        self.conversion_factor = 1.852

    def nautical_miles_to_kilometers(self, nautical_miles):
        if nautical_miles == 0:
            return 0
        return nautical_miles * self.conversion_factor

if __name__ == '__main__':
    converter = DistanceConverter()
    print(f"0 nautical miles is {converter.nautical_miles_to_kilometers(0)} kilometers")
    print(f"1 nautical mile is {converter.nautical_miles_to_kilometers(1)} kilometers")
    print(f"50 nautical miles is {converter.nautical_miles_to_kilometers(50)} kilometers")