class DistanceConverter:
    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type (int or float)")
        return miles * 5280

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.miles_to_feet(1))
    print(converter.miles_to_feet(0.5))
    print(converter.miles_to_feet(10))