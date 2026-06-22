class DistanceConverter:
    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type (int or float)")
        return miles * 5280

    @staticmethod
    def feet_to_miles(feet):
        if not isinstance(feet, (int, float)):
            raise TypeError("Input must be a numeric type (int or float)")
        return feet / 5280

if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.miles_to_feet(1))
    print(converter.miles_to_feet(2.5))
    print(converter.feet_to_miles(5280))
    print(converter.feet_to_miles(10560))
    try:
        converter.miles_to_feet("invalid")
    except TypeError as e:
        print(e)