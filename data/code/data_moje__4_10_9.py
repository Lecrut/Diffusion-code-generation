class DistanceConverter:
    MILES_TO_KM = 1.60934
    KM_TO_MILES = 1.0 / MILES_TO_KM

    @staticmethod
    def _validate_input(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a numeric value")
        if value < 0:
            raise ValueError("Distance cannot be negative")
        return float(value)

    def miles_to_kilometers(self, miles):
        validated_miles = self._validate_input(miles)
        return validated_miles * self.MILES_TO_KM

    def kilometers_to_miles(self, kilometers):
        validated_km = self._validate_input(kilometers)
        return validated_km * self.KM_TO_MILES

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.miles_to_kilometers(1))
    print(converter.kilometers_to_miles(1))
    print(converter.miles_to_kilometers(10))
    print(converter.kilometers_to_miles(10))
    print(converter.miles_to_kilometers(0))
    print(converter.kilometers_to_miles(0))