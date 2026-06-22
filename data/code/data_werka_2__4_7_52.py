class DistanceConverter:
    def __init__(self):
        self.conversion_factors = {
            ('miles', 'kilometers'): 1.60934,
            ('kilometers', 'miles'): 0.621371,
        }

    def convert(self, distance, from_unit, to_unit):
        if (from_unit, to_unit) not in self.conversion_factors:
            raise ValueError("Unsupported unit conversion")
        return distance * self.conversion_factors[(from_unit, to_unit)]

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_distance_miles = 5
    sample_distance_kilometers = 10
    converted_to_km = converter.convert(sample_distance_miles, 'miles', 'kilometers')
    converted_to_miles = converter.convert(sample_distance_kilometers, 'kilometers', 'miles')
    print(f"{sample_distance_miles} miles is {converted_to_km:.2f} kilometers")
    print(f"{sample_distance_kilometers} kilometers is {converted_to_miles:.2f} miles")