class DistanceConverter:
    MILES_TO_FEET = 5280

    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a number")
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        return miles * DistanceConverter.MILES_TO_FEET

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_miles = 10.5
    result = DistanceConverter.miles_to_feet(sample_miles)
    print(result)