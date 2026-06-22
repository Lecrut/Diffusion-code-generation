class DistanceConverter:
    def __init__(self):
        self.meters_per_mile = 1609.344
        self.feet_per_meter = 3.28084

    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a number")
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        return miles * 5280.0

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_distance_miles = 10.0
    result = converter.miles_to_feet(sample_distance_miles)
    print(result)