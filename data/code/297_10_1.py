class UnitConverter:
    def __init__(self):
        self.length_to_meter = 1.0
        self.mass_to_kilogram = 1.0
        self.volume_to_liter = 1.0
    def convert_length(self, value, from_unit, to_unit):
        if from_unit == "m" and to_unit == "m":
            return value
        elif from_unit == "km" and to_unit == "m":
            return value * 1000.0
        elif from_unit == "m" and to_unit == "km":
            return value / 1000.0
        else:
            raise ValueError("Unsupported length conversion.")
    def convert_mass(self, value, from_unit, to_unit):
        if from_unit == "kg" and to_unit == "kg":
            return value
        elif from_unit == "g" and to_unit == "kg":
            return value / 1000.0
        elif from_unit == "kg" and to_unit == "g":
            return value * 1000.0
        else:
            raise ValueError("Unsupported mass conversion.")
    def convert_volume(self, value, from_unit, to_unit):
        if from_unit == "l" and to_unit == "l":
            return value
        elif from_unit == "ml" and to_unit == "l":
            return value / 1000.0
        elif from_unit == "l" and to_unit == "ml":
            return value * 1000.0
        else:
            raise ValueError("Unsupported volume conversion.")
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversion ---")
    try:
        length_result = converter.convert_length(5, "km", "m")
        print("5 km to meters:", length_result)
        length_result_2 = converter.convert_length(1000, "m", "km")
        print("1000 meters to kilometers:", length_result_2)
    except ValueError as e:
        print(f"Error in length conversion: {e}")
    print("\n--- Mass Conversion ---")
    try:
        mass_result = converter.convert_mass(2500, "g", "kg")
        print("2500 grams to kilograms:", mass_result)
        mass_result_2 = converter.convert_mass(1.5, "kg", "g")
        print("1.5 kilograms to grams:", mass_result_2)
    except ValueError as e:
        print(f"Error in mass conversion: {e}")
    print("\n--- Volume Conversion ---")
    try:
        volume_result = converter.convert_volume(500, "ml", "l")
        print("500 ml to liters:", volume_result)
        volume_result_2 = converter.convert_volume(2.5, "l", "ml")
        print("2.5 liters to milliliters:", volume_result_2)
    except ValueError as e:
        print(f"Error in volume conversion: {e}")
    print("\n--- Error Handling Test ---")
    try:
        converter.convert_length(1, "ft", "m")
    except ValueError as e:
        print(f"Caught expected error: {e}")