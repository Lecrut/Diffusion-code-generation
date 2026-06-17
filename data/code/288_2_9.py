class TemperatureConverter:
    def to_celsius(self, value, unit):
        if unit.lower() == 'c':
            return float(value)
        elif unit.lower() == 'f':
            return (float(value) - 32) * 5 / 9
        elif unit.lower() == 'k':
            return float(value) - 273.15
        else:
            raise ValueError("Invalid unit specified. Use 'C', 'F', or 'K'.")
    def to_fahrenheit(self, value, unit):
        if unit.lower() == 'c':
            return (float(value) * 9 / 5) + 32
        elif unit.lower() == 'f':
            return float(value)
        elif unit.lower() == 'k':
            return (float(value) - 273.15) * 9 / 5 + 32
        else:
            raise ValueError("Invalid unit specified. Use 'C', 'F', or 'K'.")
    def to_kelvin(self, value, unit):
        if unit.lower() == 'c':
            return float(value) + 273.15
        elif unit.lower() == 'f':
            return (float(value) - 32) * 5 / 9 + 273.15
        elif unit.lower() == 'k':
            return float(value)
        else:
            raise ValueError("Invalid unit specified. Use 'C', 'F', or 'K'.")
if __name__ == '__main__':
    converter = TemperatureConverter()
    print("--- Celsius Conversions ---")
    c_val = 25.0
    print(f"{c_val}°C to F: {converter.to_fahrenheit(c_val, 'C'):.2f}")
    print(f"{c_val}°C to K: {converter.to_kelvin(c_val, 'C'):.2f}")
    print("\n--- Fahrenheit Conversions ---")
    f_val = 68.0
    print(f"{f_val}°F to C: {converter.to_celsius(f_val, 'F'):.2f}")
    print(f"{f_val}°F to K: {converter.to_kelvin(f_val, 'F'):.2f}")
    print("\n--- Kelvin Conversions ---")
    k_val = 300.15
    print(f"{k_val}K to C: {converter.to_celsius(k_val, 'K'):.2f}")
    print(f"{k_val}K to F: {converter.to_fahrenheit(k_val, 'K'):.2f}")
    print("\n--- Error Handling Test ---")
    try:
        converter.to_celsius(10, 'X')
    except ValueError as e:
        print(f"Caught expected error: {e}")