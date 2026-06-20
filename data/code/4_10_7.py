class DistanceConverter:
    FACTOR_MILES_TO_KM = 1.609344
    FACTOR_KM_TO_MILES = 0.621371192

    def __init__(self):
        self.miles_to_km_factor = self.FACTOR_MILES_TO_KM
        self.km_to_miles_factor = self.FACTOR_KM_TO_MILES

    def _validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Distance must be a number")
        if value < 0:
            raise ValueError("Distance cannot be negative")
        return float(value)

    def miles_to_kilometers(self, miles):
        validated = self._validate_input(miles)
        return validated * self.miles_to_km_factor

    def kilometers_to_miles(self, kilometers):
        validated = self._validate_input(kilometers)
        return validated * self.km_to_miles_factor

if __name__ == '__main__':
    converter = DistanceConverter()
    result_miles_to_km = converter.miles_to_kilometers(10)
    result_km_to_miles = converter.kilometers_to_miles(10)
    print(result_miles_to_km)
    print(result_km_to_miles)