class UnitConverter:
    @staticmethod
    def convert_miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a number.")
        if miles < 0:
            raise ValueError("Input must be non-negative.")
        return miles * 5280

if __name__ == "__main__":
    result1 = UnitConverter.convert_miles_to_feet(3)
    print(result1)
    result2 = UnitConverter.convert_miles_to_feet(1.5)
    print(result2)
    try:
        UnitConverter.convert_miles_to_feet("two")
    except TypeError as e:
        print(e)