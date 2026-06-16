class UnitConverter:
    def convert_length(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "m":
            if to_unit == "cm":
                return value * 100
            elif to_unit == "km":
                return value / 1000
        elif from_unit == "cm":
            if to_unit == "m":
                return value / 100
        elif from_unit == "km":
            if to_unit == "m":
                return value * 1000
        return None
    def convert_mass(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "kg":
            if to_unit == "g":
                return value * 1000
            elif to_unit == "mg":
                return value * 1000000
        elif from_unit == "g":
            if to_unit == "kg":
                return value / 1000
        return None
    def convert_volume(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "L":
            if to_unit == "mL":
                return value * 1000
        elif from_unit == "mL":
            if to_unit == "L":
                return value / 1000
        return None
if __name__ == '__main__':
    converter = UnitConverter()
    length_result = converter.convert_length(10, "m", "cm")
    print(f"Length conversion (10 m to cm): {length_result}")
    length_result_2 = converter.convert_length(500, "cm", "m")
    print(f"Length conversion (500 cm to m): {length_result_2}")
    mass_result = converter.convert_mass(2, "kg", "g")
    print(f"Mass conversion (2 kg to g): {mass_result}")
    mass_result_2 = converter.convert_mass(500, "g", "kg")
    print(f"Mass conversion (500 g to kg): {mass_result_2}")
    volume_result = converter.convert_volume(5, "L", "mL")
    print(f"Volume conversion (5 L to mL): {volume_result}")
    volume_result_2 = converter.convert_volume(1000, "mL", "L")
    print(f"Volume conversion (1000 mL to L): {volume_result_2}")