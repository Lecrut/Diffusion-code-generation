class TemperatureConverter:
    def to_celsius(self, value, unit):
        if unit == "C":
            return value
        elif unit == "F":
            return (value - 32) * 5 / 9
        elif unit == "K":
            return value - 273.15
        else:
            raise ValueError("Invalid unit specified. Use 'C', 'F', or 'K'.")
    def to_fahrenheit(self, value, unit):
        if unit == "C":
            return (value * 9 / 5) + 32
        elif unit == "F":
            return value
        elif unit == "K":
            return (value - 273.15) * 9 / 5 + 32
        else:
            raise ValueError("Invalid unit specified. Use 'C', 'F', or 'K'.")
    def to_kelvin(self, value, unit):
        if unit == "C":
            return value + 273.15
        elif unit == "F":
            return (value + 459.67) * 5 / 9
        elif unit == "K":
            return value
        else:
            raise ValueError("Invalid unit specified. Use 'C', 'F', or 'K'.")
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_temp = 25.0
    fahrenheit_temp = 77.0
    kelvin_temp = 298.15
    print(f"--- Converting Celsius to others ---")
    print(f"{celsius_temp}°C is {converter.to_fahrenheit(celsius_temp, 'C'):.2f}°F")
    print(f"{celsius_temp}°C is {converter.to_kelvin(celsius_temp, 'C'):.2f}K")
    print(f"\n--- Converting Fahrenheit to others ---")
    print(f"{fahrenheit_temp}°F is {converter.to_celsius(fahrenheit_temp, 'F'):.2f}°C")
    print(f"{fahrenheit_temp}°F is {converter.to_kelvin(fahrenheit_temp, 'F'):.2f}K")
    print(f"\n--- Converting Kelvin to others ---")
    print(f"{kelvin_temp}K is {converter.to_celsius(kelvin_temp, 'K'):.2f}°C")
    print(f"{kelvin_temp}K is {converter.to_fahrenheit(kelvin_temp, 'K'):.2f}°F")
    print(f"\n--- Error Handling Test ---")
    try:
        converter.to_celsius(10, "R")
    except ValueError as e:
        print(f"Caught expected error: {e}")