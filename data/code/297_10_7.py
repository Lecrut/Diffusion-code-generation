class UnitConverter:
    def __init__(self):
        self.length_to_meter = 1.0
        self.mass_to_kilogram = 1.0
        self.volume_to_liter = 1.0
    def convert_length(self, value, from_unit, to_unit):
        if from_unit == "meter" and to_unit == "meter":
            return value
        elif from_unit == "meter":
            if to_unit == "kilometer":
                return value / 1000.0
            elif to_unit == "centimeter":
                return value * 100.0
            else:
                raise ValueError("Unsupported length conversion target.")
        elif from_unit == "kilometer":
            if to_unit == "meter":
                return value * 1000.0
            elif to_unit == "centimeter":
                return value * 100000.0
            else:
                raise ValueError("Unsupported length conversion target.")
        elif from_unit == "centimeter":
            if to_unit == "meter":
                return value / 100.0
            elif to_unit == "kilometer":
                return value / 1000.0
            else:
                raise ValueError("Unsupported length conversion target.")
        else:
            raise ValueError(f"Unsupported starting length unit: {from_unit}")
    def convert_mass(self, value, from_unit, to_unit):
        if from_unit == "kilogram" and to_unit == "kilogram":
            return value
        elif from_unit == "kilogram":
            if to_unit == "gram":
                return value * 1000.0
            else:
                raise ValueError("Unsupported mass conversion target.")
        elif from_unit == "gram":
            if to_unit == "kilogram":
                return value / 1000.0
            else:
                raise ValueError("Unsupported mass conversion target.")
        else:
            raise ValueError(f"Unsupported starting mass unit: {from_unit}")
    def convert_volume(self, value, from_unit, to_unit):
        if from_unit == "liter" and to_unit == "liter":
            return value
        elif from_unit == "liter":
            if to_unit == "milliliter":
                return value * 1000.0
            else:
                raise ValueError("Unsupported volume conversion target.")
        elif from_unit == "milliliter":
            if to_unit == "liter":
                return value / 1000.0
            else:
                raise ValueError("Unsupported volume conversion target.")
        else:
            raise ValueError(f"Unsupported starting volume unit: {from_unit}")
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversion ---")
    try:
        length_result = converter.convert_length(10, "meter", "kilometer")
        print("10 meters is:", length_result, "kilometers")
        length_result_2 = converter.convert_length(500, "centimeter", "meter")
        print("500 centimeters is:", length_result_2, "meters")
        length_result_3 = converter.convert_length(2000, "kilometer", "meter")
        print("2000 kilometers is:", length_result_3, "meters")
    except ValueError as e:
        print(f"Error during length conversion: {e}")
    print("\n--- Mass Conversion ---")
    try:
        mass_result = converter.convert_mass(5000, "kilogram", "gram")
        print("5000 kilograms is:", mass_result, "grams")
        mass_result_2 = converter.convert_mass(2500, "gram", "kilogram")
        print("2500 grams is:", mass_result_2, "kilograms")
    except ValueError as e:
        print(f"Error during mass conversion: {e}")
    print("\n--- Volume Conversion ---")
    try:
        volume_result = converter.convert_volume(2.5, "liter", "milliliter")
        print("2.5 liters is:", volume_result, "milliliters")
        volume_result_2 = converter.convert_volume(500, "milliliter", "liter")
        print("500 milliliters is:", volume_result_2, "liters")
    except ValueError as e:
        print(f"Error during volume conversion: {e}")