class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371

    def __init__(self):
        self._mile_factor = self.MILES_TO_KILOMETERS
        self._km_factor = self.KILOMETERS_TO_MILES

    def validate_distance(self, distance):
        if not isinstance(distance, (int, float)):
            raise TypeError("Distance must be a numeric value.")
        if distance < 0:
            raise ValueError("Distance cannot be negative.")

    def miles_to_kilometers(self, miles):
        self.validate_distance(miles)
        return miles * self._mile_factor

    def kilometers_to_miles(self, kilometers):
        self.validate_distance(kilometers)
        return kilometers * self._km_factor

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_miles = 10.0
    sample_km = 16.0934

    result_km = converter.miles_to_kilometers(sample_miles)
    result_miles = converter.kilometers_to_miles(sample_km)

    print(result_km)
    print(result_miles)