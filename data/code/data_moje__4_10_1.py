class DistanceConverter:
    MILES_TO_KM = 1.609344
    KM_TO_MILES = 1 / 1.609344

    @staticmethod
    def _validate_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Distance must be a number.")
        if value < 0:
            raise ValueError("Distance cannot be negative.")
        return float(value)

    @staticmethod
    def miles_to_kilometers(miles):
        validated_miles = DistanceConverter._validate_value(miles)
        return validated_miles * DistanceConverter.MILES_TO_KM

    @staticmethod
    def kilometers_to_miles(kilometers):
        validated_km = DistanceConverter._validate_value(kilometers)
        return validated_km * DistanceConverter.KM_TO_MILES

if __name__ == '__main__':
    converter = DistanceConverter()
    miles_val = 50
    km_val = 80.4672
    km_result = DistanceConverter.miles_to_kilometers(miles_val)
    miles_result = DistanceConverter.kilometers_to_miles(km_val)
    print(f"{miles_val} miles is {km_result} kilometers")
    print(f"{km_val} kilometers is {miles_result} miles")