class UnitConverter:
    def to_length(self, value, unit):
        unit = unit.lower()
        if unit == 'm':
            return value
        elif unit == 'km':
            return value * 1000
        elif unit == 'cm':
            return value / 100
        elif unit == 'mm':
            return value / 1000
        else:
            raise ValueError("Unsupported length unit")
    def from_length(self, value, unit):
        unit = unit.lower()
        if unit == 'm':
            return value
        elif unit == 'km':
            return value / 1000
        elif unit == 'cm':
            return value * 100
        elif unit == 'mm':
            return value * 1000
        else:
            raise ValueError("Unsupported length unit")
    def to_mass(self, value, unit):
        unit = unit.lower()
        if unit == 'kg':
            return value
        elif unit == 'g':
            return value / 1000
        elif unit == 'mg':
            return value / 1000000
        else:
            raise ValueError("Unsupported mass unit")
    def from_mass(self, value, unit):
        unit = unit.lower()
        if unit == 'kg':
            return value
        elif unit == 'g':
            return value * 1000
        elif unit == 'mg':
            return value * 1000000
        else:
            raise ValueError("Unsupported mass unit")
    def to_volume(self, value, unit):
        unit = unit.lower()
        if unit == 'l':
            return value
        elif unit == 'ml':
            return value * 1000
        elif unit == 'm3':
            return value * 1000000
        else:
            raise ValueError("Unsupported volume unit")
    def from_volume(self, value, unit):
        unit = unit.lower()
        if unit == 'l':
            return value
        elif unit == 'ml':
            return value / 1000
        elif unit == 'm3':
            return value / 1000000
        else:
            raise ValueError("Unsupported volume unit")
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversions ---")
    length_val = 5
    print(f"{length_val} m to km: {converter.to_length(length_val, 'm')}")
    print(f"10 km to m: {converter.from_length(10, 'km')}")
    print(f"250 cm to m: {converter.from_length(250, 'cm')}")
    print("\n--- Mass Conversions ---")
    mass_val = 2.5
    print(f"{mass_val} kg to g: {converter.to_mass(mass_val, 'kg')}")
    print(f"500 g to kg: {converter.from_mass(500, 'g')}")
    print(f"1500000 mg to kg: {converter.from_mass(1500000, 'mg')}")
    print("\n--- Volume Conversions ---")
    volume_val = 2
    print(f"{volume_val} l to ml: {converter.to_volume(volume_val, 'l')}")
    print(f"5000 ml to l: {converter.from_volume(5000, 'ml')}")
    print(f"1 m3 to l: {converter.from_volume(1, 'm3')}")
    print("\n--- Error Handling Test ---")
    try:
        converter.to_length(10, 'inch')
    except ValueError as e:
        print(f"Caught expected error: {e}")