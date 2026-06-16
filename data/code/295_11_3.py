class UnitConverter:
    def convert_mass(self, value, unit, target_unit):
        if unit in ["kg", "lb"]:
            if target_unit in ["kg", "lb"]:
                if unit == target_unit:
                    return value
                elif unit == "kg" and target_unit == "lb":
                    return value * 2.20462
                elif unit == "lb" and target_unit == "kg":
                    return value / 2.20462
        return None
    def convert_volume(self, value, unit, target_unit):
        if unit in ["L", "gal"]:
            if target_unit in ["L", "gal"]:
                if unit == target_unit:
                    return value
                elif unit == "L" and target_unit == "gal":
                    return value * 0.264172
                elif unit == "gal" and target_unit == "L":
                    return value / 0.264172
        return None
if __name__ == '__main__':
    converter = UnitConverter()
    mass_kg = 10
    mass_lb = 22.0462
    print(f"Mass Conversion: {mass_kg} kg to lb is {converter.convert_mass(mass_kg, 'kg', 'lb'):.2f} lb")
    print(f"Mass Conversion: {mass_lb} lb to kg is {converter.convert_mass(mass_lb, 'lb', 'kg'):.2f} kg")
    volume_L = 10
    volume_gal = 26.4172
    print(f"Volume Conversion: {volume_L} L to gal is {converter.convert_volume(volume_L, 'L', 'gal'):.2f} gal")
    print(f"Volume Conversion: {volume_gal} gal to L is {converter.convert_volume(volume_gal, 'gal', 'L'):.2f} L")