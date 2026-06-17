class UnitConverter:
    def __init__(self):
        self.length_conversions = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.34
        }
        self.mass_conversions = {
            'kg': 1.0,
            'g': 0.001,
            'mg': 0.000001,
            'lb': 0.453592
        }
        self.volume_conversions = {
            'L': 1.0,
            'mL': 0.001,
            'm3': 1.0,
            'gal': 3.78541
        }
    def convert_length(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.length_conversions or to_unit not in self.length_conversions:
            raise ValueError("Invalid unit specified for length conversion.")
        if from_unit == to_unit:
            return value
        base_value = value * self.length_conversions[from_unit]
        result = base_value / self.length_conversions[to_unit]
        return result
    def convert_mass(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.mass_conversions or to_unit not in self.mass_conversions:
            raise ValueError("Invalid unit specified for mass conversion.")
        if from_unit == to_unit:
            return value
        base_value = value * self.mass_conversions[from_unit]
        result = base_value / self.mass_conversions[to_unit]
        return result
    def convert_volume(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.volume_conversions or to_unit not in self.volume_conversions:
            raise ValueError("Invalid unit specified for volume conversion.")
        if from_unit == to_unit:
            return value
        base_value = value * self.volume_conversions[from_unit]
        result = base_value / self.volume_conversions[to_unit]
        return result
if __name__ == '__main__':
    converter = UnitConverter()
    print("--- Length Conversion (10 meters to kilometers) ---")
    try:
        length_result = converter.convert_length(10.0, 'm', 'km')
        print(f"10.0 m is equal to {length_result:.2f} km")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Length Conversion (100 cm to mm) ---")
    try:
        length_result = converter.convert_length(100.0, 'cm', 'mm')
        print(f"100.0 cm is equal to {length_result:.2f} mm")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Mass Conversion (5 kg to grams) ---")
    try:
        mass_result = converter.convert_mass(5.0, 'kg', 'g')
        print(f"5.0 kg is equal to {mass_result:.2f} g")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Mass Conversion (10 lb to kg) ---")
    try:
        mass_result = converter.convert_mass(10.0, 'lb', 'kg')
        print(f"10.0 lb is equal to {mass_result:.2f} kg")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Volume Conversion (2 L to mL) ---")
    try:
        volume_result = converter.convert_volume(2.0, 'L', 'mL')
        print(f"2.0 L is equal to {volume_result:.2f} mL")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Volume Conversion (1 m3 to L) ---")
    try:
        volume_result = converter.convert_volume(1.0, 'm3', 'L')
        print(f"1.0 m3 is equal to {volume_result:.2f} L")
    except ValueError as e:
        print(f"Error: {e}")
    print("\n--- Error Handling Test ---")
    try:
        converter.convert_length(10.0, 'm', 'ft')
    except ValueError as e:
        print(f"Caught expected error: {e}")