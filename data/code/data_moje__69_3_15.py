class UnitConverter:
    @staticmethod
    def convert_miles_to_feet(miles):
        if not isinstance(miles, (int, float)):
            raise TypeError("Input must be a numeric type (int or float).")
        if isinstance(miles, bool):
            raise TypeError("Input must be a numeric type (int or float), not a boolean.")
        feet = miles * 5280
        return feet

if __name__ == '__main__':
    miles_value = 10
    result = UnitConverter.convert_miles_to_feet(miles_value)
    print(f"{miles_value} miles is {result} feet.")
    miles_value_float = 2.5
    result_float = UnitConverter.convert_miles_to_feet(miles_value_float)
    print(f"{miles_value_float} miles is {result_float} feet.")
    try:
        UnitConverter.convert_miles_to_feet("invalid")
    except TypeError as e:
        print(f"Error caught: {e}")