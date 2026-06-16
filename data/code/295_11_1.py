class UnitConverter:
    def convert_mass(self, value, from_unit, to_unit):
        if from_unit == 'kg' and to_unit == 'lb':
            return value * 2.2046226
        elif from_unit == 'lb' and to_unit == 'kg':
            return value / 2.2046226
        return None
    def convert_volume(self, value, from_unit, to_unit):
        if from_unit == 'L' and to_unit == 'gal':
            return value * 0.264172
        elif from_unit == 'gal' and to_unit == 'L':
            return value / 0.264172
        return None
if __name__ == '__main__':
    converter = UnitConverter()
    mass_kg = 10
    mass_lb = converter.convert_mass(mass_kg, 'kg', 'lb')
    print(f"{mass_kg} kg is {mass_lb:.2f} lb")
    mass_lb_to_kg = 50
    mass_kg_from_lb = converter.convert_mass(mass_lb_to_kg, 'lb', 'kg')
    print(f"{mass_lb_to_kg} lb is {mass_kg_from_lb:.2f} kg")
    volume_L = 10
    volume_gal = converter.convert_volume(volume_L, 'L', 'gal')
    print(f"{volume_L} L is {volume_gal:.2f} gal")
    volume_gal_to_L = 5
    volume_L_from_gal = converter.convert_volume(volume_gal_to_L, 'gal', 'L')
    print(f"{volume_gal_to_L} gal is {volume_L_from_gal:.2f} L")