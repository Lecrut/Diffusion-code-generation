class UnitConverter:
    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type (int or float)")
        if miles < 0:
            raise ValueError("Input must be a non-negative number")
        return miles * 5280

if __name__ == '__main__':
    converter = UnitConverter()
    result1 = converter.miles_to_feet(2.5)
    print(result1)
    try:
        result2 = converter.miles_to_feet("invalid")
        print(result2)
    except TypeError as e:
        print(e)
    try:
        result3 = converter.miles_to_feet(-5)
        print(result3)
    except ValueError as e:
        print(e)