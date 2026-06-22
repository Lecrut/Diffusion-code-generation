class DistanceConverter:
    def __init__(self):
        self.miles_to_km_factor = 1.609344
        self.km_to_miles_factor = 0.621371192

    def _validate_distance(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Distance must be a numeric type (int or float).")
        if value < 0:
            raise ValueError("Distance cannot be negative.")
        return True

    def miles_to_km(self, miles):
        self._validate_distance(miles)
        return miles * self.miles_to_km_factor

    def km_to_miles(self, km):
        self._validate_distance(km)
        return km * self.km_to_miles_factor

if __name__ == '__main__':
    converter = DistanceConverter()
    result_miles_to_km = converter.miles_to_km(10)
    result_km_to_miles = converter.km_to_miles(10)
    print(result_miles_to_km)
    print(result_km_to_miles)