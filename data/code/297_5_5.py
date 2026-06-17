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
                raise ValueError("Invalid length unit provided.")
            base_value = value * self.length_factors[from_unit]
            result = base_value / self.length_factors[to_unit]
            return result
        elif type == "mass":
            if from_unit not in self.mass_factors or to_unit not in self.mass_factors:
                raise ValueError("Invalid mass unit provided.")
            base_value = value * self.mass_factors[from_unit]
            result = base_value / self.mass_factors[to_unit]
            return result
        else:
            raise ValueError("Invalid type specified. Must be 'length' or 'mass'.")
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversion ---")
    try:
        length_value = 10
        from_unit = "meter"
        to_unit = "kilometer"
        result = converter.convert(length_value, from_unit, to_unit, "length")
        print(f"{length_value} {from_unit} is equal to {result:.4f} {to_unit}")
        length_value = 1
        from_unit = "mile"
        to_unit = "foot"
        result = converter.convert(length_value, from_unit, to_unit, "length")
        print(f"{length_value} {from_unit} is equal to {result:.4f} {to_unit}")
    except ValueError as e:
        print(f"Error during length conversion: {e}")
    print("\n--- Mass Conversion ---")
    try:
        mass_value = 500
        from_unit = "kilogram"
        to_unit = "gram"
        result = converter.convert(mass_value, from_unit, to_unit, "mass")
        print(f"{mass_value} {from_unit} is equal to {result:.2f} {to_unit}")
        mass_value = 10
        from_unit = "pound"
        to_unit = "ounce"
        result = converter.convert(mass_value, from_unit, to_unit, "mass")
        print(f"{mass_value} {from_unit} is equal to {result:.2f} {to_unit}")
    except ValueError as e:
        print(f"Error during mass conversion: {e}")