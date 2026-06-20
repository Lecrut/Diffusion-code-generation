class DistanceConverter:
    MILES_TO_KM = 1.60934

    def miles_to_kilometers(self, miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Value must be a number")
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        return miles * self.MILES_TO_KM

    def kilometers_to_miles(self, kilometers):
        if not isinstance(kilometers, (int, float)):
            raise TypeError("Value must be a number")
        if kilometers < 0:
            raise ValueError("Distance cannot be negative")
        return kilometers / self.MILES_TO_KM

if __name__ == '__main__':
    converter = DistanceConverter()
    test_miles = 55.0
    test_km = 100.0
    miles_result = converter.miles_to_kilometers(test_miles)
    km_result = converter.kilometers_to_miles(test_km)
    print(miles_result)
    print(km_result)