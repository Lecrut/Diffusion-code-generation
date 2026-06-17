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
            raise NotImplementedError(f"Conversion from {from_unit} to {to_unit} is not implemented in this simple example.")
if __name__ == '__main__':
    conversion_data = {
        "length": {
            "meter": 1.0,
            "kilometer": 1000.0,
            "centimeter": 100.0,
            "mile": 1609.34
        },
        "mass": {
            "kilogram": 1.0,
            "gram": 1000.0,
            "pound": 2.20462
        }
    }
    converter = UnitConverter(conversion_data)
    print("--- Length Conversions ---")
    try:
        value_m = 5.0
        result_km = converter.convert(value_m, "meter", "kilometer")
        print(f"{value_m} meters is {result_km} kilometers")
        value_cm = 250.0
        result_m = converter.convert(value_cm, "centimeter", "meter")
        print(f"{value_cm} centimeters is {result_m} meters")
        value_mi = 1.0
        result_km_from_mi = converter.convert(value_mi, "mile", "kilometer")
        print(f"{value_mi} mile is {result_km_from_mi} kilometers")
    except (ValueError, NotImplementedError) as e:
        print(f"Error during length conversion: {e}")
    print("\n--- Mass Conversions ---")
    try:
        value_kg = 2.5
        result_g = converter.convert(value_kg, "kilogram", "gram")
        print(f"{value_kg} kilograms is {result_g} grams")
        value_lb = 10.0
        result_kg = converter.convert(value_lb, "pound", "kilogram")
        print(f"{value_lb} pounds is {result_kg} kilograms")
    except (ValueError, NotImplementedError) as e:
        print(f"Error during mass conversion: {e}")