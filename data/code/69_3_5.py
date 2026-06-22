class UnitConverter:
    @staticmethod
    def miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type (int or float).")
        if miles < 0:
            raise ValueError("Input must be a non-negative number.")
        return miles * 5280

if __name__ == '__main__':
    result1 = UnitConverter.miles_to_feet(2.5)
    print(result1)
    result2 = UnitConverter.miles_to_feet(10)
    print(result2)
    try:
        result3 = UnitConverter.miles_to_feet("invalid")
        print(result3)
    except TypeError as e:
        print(e)