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
    length_value = 10.0
    try:
        m_to_in = converter.convert_length(length_value, "m", "in")
        print(f"{length_value} m is {m_to_in:.4f} in")
        in_to_m = converter.convert_length(m_to_in, "in", "m")
        print(f"{m_to_in:.4f} in is {in_to_m:.4f} m")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Mass Conversion (kg <-> lb) ---")
    mass_value = 10.0
    try:
        kg_to_lb = converter.convert_mass(mass_value, "kg", "lb")
        print(f"{mass_value} kg is {kg_to_lb:.4f} lb")
        lb_to_kg = converter.convert_mass(kg_to_lb, "lb", "kg")
        print(f"{kg_to_lb:.4f} lb is {lb_to_kg:.4f} kg")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Volume Conversion (L <-> gal) ---")
    volume_value = 5.0
    try:
        L_to_gal = converter.convert_volume(volume_value, "L", "gal")
        print(f"{volume_value} L is {L_to_gal:.4f} gal")
        gal_to_L = converter.convert_volume(L_to_gal, "gal", "L")
        print(f"{L_to_gal:.4f} gal is {gal_to_L:.4f} L")
    except ValueError as e:
        print(f"Error: {e}")