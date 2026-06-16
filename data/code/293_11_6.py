class UnitConverter:
    def convert_length(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit == to_unit:
            return value
        if from_unit == "meter" and to_unit == "inch":
            return value * 39.3701
        elif from_unit == "inch" and to_unit == "meter":
            return value / 39.3701
        elif from_unit == "kilometer" and to_unit == "mile":
            return value * 0.621371
        elif from_unit == "mile" and to_unit == "kilometer":
            return value / 0.621371
        else:
            raise ValueError("Unsupported length conversion")
    def convert_mass(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit == to_unit:
            return value
        if from_unit == "kilogram" and to_unit == "pound":
            return value * 2.20462
        elif from_unit == "pound" and to_unit == "kilogram":
            return value / 2.20462
        else:
            raise ValueError("Unsupported mass conversion")
    def convert_volume(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit == to_unit:
            return value
        if from_unit == "liter" and to_unit == "gallon":
            return value * 0.264172
        elif from_unit == "gallon" and to_unit == "liter":
            return value / 0.264172
        else:
            raise ValueError("Unsupported volume conversion")
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversion ---")
    length_value = 10.0
    try:
        meters_to_inches = converter.convert_length(length_value, "meter", "inch")
        print(f"{length_value} meter is {meters_to_inches:.4f} inch")
        km_to_miles = converter.convert_length(5.0, "kilometer", "mile")
        print(f"5.0 kilometer is {km_to_miles:.4f} mile")
    except ValueError as e:
        print(f"Error in length conversion: {e}")
    print("\n--- Mass Conversion ---")
    mass_value = 10.0
    try:
        kg_to_lb = converter.convert_mass(mass_value, "kilogram", "pound")
        print(f"{mass_value} kilogram is {kg_to_lb:.4f} pound")
    except ValueError as e:
        print(f"Error in mass conversion: {e}")
    print("\n--- Volume Conversion ---")
    volume_value = 5.0
    try:
        liters_to_gallons = converter.convert_volume(volume_value, "liter", "gallon")
        print(f"{volume_value} liter is {liters_to_gallons:.4f} gallon")
    except ValueError as e:
        print(f"Error in volume conversion: {e}")