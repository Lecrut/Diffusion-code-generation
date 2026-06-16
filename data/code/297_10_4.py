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
        elif from_unit == "cm" and to_unit == "m":
            return value / 100.0
        elif from_unit == "m" and to_unit == "cm":
            return value * 100.0
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
        if from_unit == "L" and to_unit == "L":
            return value
        elif from_unit == "m3" and to_unit == "L":
            return value * 1000.0
        elif from_unit == "L" and to_unit == "m3":
            return value / 1000.0
        else:
            raise ValueError("Unsupported volume conversion.")
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversion ---")
    try:
        length_result = converter.convert_length(10, "m", "km")
        print("10 meters to kilometers:", length_result)
        length_result = converter.convert_length(500, "cm", "m")
        print("500 centimeters to meters:", length_result)
    except ValueError as e:
        print(f"Error in length conversion: {e}")
    print("\n--- Mass Conversion ---")
    try:
        mass_result = converter.convert_mass(2, "kg", "g")
        print("2 kilograms to grams:", mass_result)
    except ValueError as e:
        print(f"Error in mass conversion: {e}")
    print("\n--- Volume Conversion ---")
    try:
        volume_result = converter.convert_volume(5, "m3", "L")
        print("5 cubic meters to liters:", volume_result)
    except ValueError as e:
        print(f"Error in volume conversion: {e}")