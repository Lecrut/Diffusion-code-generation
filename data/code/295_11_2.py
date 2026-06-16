class UnitConverter:
    def convert_mass(self, value, unit):
        if unit == 'kg':
            if value == 'lb':
                return value * 2.20462
            return value
        elif unit == 'lb':
            if value == 'kg':
                return value / 2.20462
            return value
        return value
    def convert_volume(self, value, unit):
        if unit == 'L':
            if value == 'gal':
                return value * 0.264172
            return value
        elif unit == 'gal':
            if value == 'L':
                return value / 0.264172
            return value
        return value
if __name__ == '__main__':
    converter = UnitConverter()
    mass_kg = 10
    mass_lb = converter.convert_mass(mass_kg, 'lb')
    print(f"{mass_kg} kg is equal to {mass_lb:.2f} lb")
    mass_lb_to_kg = 50
    mass_kg_from_lb = converter.convert_mass(mass_lb_to_kg, 'kg')
    print(f"{mass_lb_to_kg} kg is equal to {mass_kg_from_lb:.2f} lb")
    volume_L = 10
    volume_gal = converter.convert_volume(volume_L, 'gal')
    print(f"{volume_L} L is equal to {volume_gal:.2f} gal")
    volume_gal_to_L = 5
    volume_L_from_gal = converter.convert_volume(volume_gal_to_L, 'L')
    print(f"{volume_gal_to_L} L is equal to {volume_L_from_gal:.2f} gal")