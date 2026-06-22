class DistanceConverter:
    MILES_TO_FEET_RATIO = 5280

    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a number")
        if miles < 0:
            raise ValueError("Distance cannot be negative")
        return miles * DistanceConverter.MILES_TO_FEET_RATIO

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.miles_to_feet(1))
    print(converter.miles_to_feet(2.5))
    print(converter.miles_to_feet(0))