class DistanceConverter:
    MILES_TO_KM = 1.60934
    KM_TO_MILES = 0.621371

    @staticmethod
    def miles_to_kilometers(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric value.")
        if miles < 0:
            raise ValueError("Distance cannot be negative.")
        return miles * DistanceConverter.MILES_TO_KM

    @staticmethod
    def kilometers_to_miles(kilometers):
        if not isinstance(kilometers, (int, float)):
            raise TypeError("Input must be a numeric value.")
        if kilometers < 0:
            raise ValueError("Distance cannot be negative.")
        return kilometers * DistanceConverter.KM_TO_MILES

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.miles_to_kilometers(5))
    print(converter.kilometers_to_miles(10))