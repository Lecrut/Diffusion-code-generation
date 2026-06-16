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
    print(f"{length_value} meters to inches: {converter.convert_length(length_value, 'm', 'in'):.4f} inches")
    print(f"{length_value} inches to meters: {converter.convert_length(length_value, 'in', 'm'):.4f} meters")
    print("\n--- Length Conversion (km <-> mi) ---")
    length_value = 1.0
    print(f"{length_value} kilometers to miles: {converter.convert_length(length_value, 'km', 'mi'):.4f} miles")
    print(f"{length_value} miles to kilometers: {converter.convert_length(length_value, 'mi', 'km'):.4f} kilometers")
    print("\n--- Mass Conversion (kg <-> lb) ---")
    mass_value = 10.0
    print(f"{mass_value} kilograms to pounds: {converter.convert_mass(mass_value, 'kg', 'lb'):.4f} pounds")
    print(f"{mass_value} pounds to kilograms: {converter.convert_mass(mass_value, 'lb', 'kg'):.4f} kilograms")
    print("\n--- Volume Conversion (L <-> gal) ---")
    volume_value = 5.0
    print(f"{volume_value} liters to gallons: {converter.convert_volume(volume_value, 'L', 'gal'):.4f} gallons")
    print(f"{volume_value} gallons to liters: {converter.convert_volume(volume_value, 'gal', 'L'):.4f} liters")