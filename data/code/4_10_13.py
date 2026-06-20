class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371

    @staticmethod
    def _validate_distance(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Distance must be a number.")
        if value < 0:
            raise ValueError("Distance cannot be negative.")

    def miles_to_kilometers(self, miles):
        self._validate_distance(miles)
        return miles * self.MILES_TO_KILOMETERS

    def kilometers_to_miles(self, kilometers):
        self._validate_distance(kilometers)
        return kilometers * self.KILOMETERS_TO_MILES

if __name__ == '__main__':
    converter = DistanceConverter()
    miles_value = 100
    km_value = 100
    
    result_km = converter.miles_to_kilometers(miles_value)
    result_miles = converter.kilometers_to_miles(km_value)
    
    print(f"{miles_value} miles is {result_km} kilometers")
    print(f"{km_value} kilometers is {result_miles} miles")