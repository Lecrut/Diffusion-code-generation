class UnitConverter:
    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("One or both units are not defined in the conversion factors.")
        if from_unit == "meter" and to_unit == "kilometer":
            return value / 1000.0
        elif from_unit == "kilometer" and to_unit == "meter":
            return value * 1000.0
        elif from_unit == "centimeter" and to_unit == "meter":
            return value / 100.0
        elif from_unit == "meter" and to_unit == "centimeter":
            return value * 100.0
        else:
            raise NotImplementedError(f"Conversion from {from_unit} to {to_unit} is not implemented in this sample.")
    def get_factors(self):
        return self.conversion_factors
if __name__ == '__main__':
    CONVERSION_DATA = {
        ("meter", "kilometer"): 1000.0,
        ("kilometer", "meter"): 1.0 / 1000.0,
        ("meter", "centimeter"): 100.0,
        ("centimeter", "meter"): 1.0 / 100.0,
    }
    converter = UnitConverter(CONVERSION_DATA)
    print("--- Testing Unit Conversion ---")
    try:
        value1 = 5.5
        result1 = converter.convert(value1, "meter", "kilometer")
        print(f"{value1} meters is {result1} kilometers")
        value2 = 2.5
        result2 = converter.convert(value2, "kilometer", "meter")
        print(f"{value2} kilometers is {result2} meters")
        value3 = 10.0
        result3 = converter.convert(value3, "meter", "centimeter")
        print(f"{value3} meters is {result3} centimeters")
        value4 = 50.0
        result4 = converter.convert(value4, "centimeter", "meter")
        print(f"{value4} centimeters is {result4} meters")
        value5 = 100
        result5 = converter.convert(value5, "meter", "meter")
        print(f"{value5} meters is {result5} meters")
        try:
            converter.convert(10, "meter", "furlong")
        except NotImplementedError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")