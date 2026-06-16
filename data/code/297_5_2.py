class UnitConverter:
    def __init__(self):
        self.length_factors = {
            "meter": 1.0,
            "kilometer": 1000.0,
            "centimeter": 0.01,
            "mile": 1609.34,
            "foot": 0.3048,
            "inch": 0.0254
        }
        self.mass_factors = {
            "kilogram": 1.0,
            "gram": 0.001,
            "milligram": 0.000001,
            "pound": 0.453592,
            "ounce": 0.0283495
        }
    def convert(self, value, from_unit, to_unit, type):
        if type == "length":
            if from_unit not in self.length_factors or to_unit not in self.length_factors:
                raise ValueError("Invalid length unit specified.")
            base_value = value * self.length_factors[from_unit]
            result = base_value / self.length_factors[to_unit]
            return result
        elif type == "mass":
            if from_unit not in self.mass_factors or to_unit not in self.mass_factors:
                raise ValueError("Invalid mass unit specified.")
            base_value = value * self.mass_factors[from_unit]
            result = base_value / self.mass_factors[to_unit]
            return result
        else:
            raise ValueError("Invalid type specified. Must be 'length' or 'mass'.")
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversions ---")
    try:
        val_m = 500.0
        result_km = converter.convert(val_m, "meter", "kilometer", "length")
        print(f"{val_m} meters is equal to {result_km:.4f} kilometers")
        val_mi = 1.0
        result_ft = converter.convert(val_mi, "mile", "foot", "length")
        print(f"{val_mi} mile is equal to {result_ft:.4f} feet")
        val_cm = 10.0
        result_in = converter.convert(val_cm, "centimeter", "inch", "length")
        print(f"{val_cm} centimeter is equal to {result_in:.4f} inches")
    except ValueError as e:
        print(f"Error during length conversion: {e}")
    print("\n--- Mass Conversions ---")
    try:
        val_kg = 2.5
        result_g = converter.convert(val_kg, "kilogram", "gram", "mass")
        print(f"{val_kg} kilogram is equal to {result_g:.4f} grams")
        val_lb = 10.0
        result_kg = converter.convert(val_lb, "pound", "kilogram", "mass")
        print(f"{val_lb} pound is equal to {result_kg:.4f} kilograms")
    except ValueError as e:
        print(f"Error during mass conversion: {e}")
    print("\n--- Error Handling Example ---")
    try:
        converter.convert(10, "meter", "kilogram", "length")
    except ValueError as e:
        print(f"Caught expected error: {e}")