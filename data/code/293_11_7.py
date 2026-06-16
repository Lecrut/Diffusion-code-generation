class UnitConverter:
    def convert_length(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit == to_unit:
            return value
        if from_unit == "m" and to_unit == "in":
            return value * 39.3701
        elif from_unit == "in" and to_unit == "m":
            return value / 39.3701
        elif from_unit == "km" and to_unit == "mi":
            return value * 0.621371
        elif from_unit == "mi" and to_unit == "km":
            return value / 0.621371
        else:
            raise ValueError("Unsupported length unit conversion")
    def convert_mass(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit == to_unit:
            return value
        if from_unit == "kg" and to_unit == "lb":
            return value * 2.20462
        elif from_unit == "lb" and to_unit == "kg":
            return value / 2.20462
        else:
            raise ValueError("Unsupported mass unit conversion")
    def convert_volume(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit == to_unit:
            return value
        if from_unit == "L" and to_unit == "gal":
            return value * 0.264172
        elif from_unit == "gal" and to_unit == "L":
            return value / 0.264172
        else:
            raise ValueError("Unsupported volume unit conversion")
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversion (m <-> in) ---")
    length_m = 10.0
    length_in = converter.convert_length(length_m, "m", "in")
    print(f"{length_m} m is equal to {length_in:.4f} in")
    length_in_to_m = 30.0
    length_m_from_in = converter.convert_length(length_in_to_m, "in", "m")
    print(f"{length_in_to_m} in is equal to {length_m_from_in:.4f} m")
    print("\n--- Length Conversion (km <-> mi) ---")
    length_km = 5.0
    length_mi = converter.convert_length(length_km, "km", "mi")
    print(f"{length_km} km is equal to {length_mi:.4f} mi")
    print("\n--- Mass Conversion (kg <-> lb) ---")
    mass_kg = 10.0
    mass_lb = converter.convert_mass(mass_kg, "kg", "lb")
    print(f"{mass_kg} kg is equal to {mass_lb:.4f} lb")
    mass_lb_to_kg = 150.0
    mass_kg_from_lb = converter.convert_mass(mass_lb_to_kg, "lb", "kg")
    print(f"{mass_lb_to_kg} lb is equal to {mass_kg_from_lb:.4f} kg")
    print("\n--- Volume Conversion (L <-> gal) ---")
    volume_L = 10.0
    volume_gal = converter.convert_volume(volume_L, "L", "gal")
    print(f"{volume_L} L is equal to {volume_gal:.4f} gal")
    volume_gal_to_L = 5.0
    volume_L_from_gal = converter.convert_volume(volume_gal_to_L, "gal", "L")
    print(f"{volume_gal_to_L} gal is equal to {volume_L_from_gal:.4f} L")