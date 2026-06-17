class TemperatureConverter:
    def to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return (celsius * 9 / 5) + 32
    def to_kelvin(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return celsius + 273.15
    def to_celsius(self, fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Input must be a number.")
        return (fahrenheit - 32) * 5 / 9
    def to_fahrenheit_from_kelvin(self, kelvin):
        if not isinstance(kelvin, (int, float)):
            raise TypeError("Input must be a number.")
        return (kelvin - 273.15) * 9 / 5 + 32
    def to_celsius_from_kelvin(self, kelvin):
        if not isinstance(kelvin, (int, float)):
            raise TypeError("Input must be a number.")
        return kelvin - 273.15
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_values = [0, 100, -40]
    print("Celsius to Fahrenheit:")
    for val in celsius_values:
        try:
            f_val = converter.to_fahrenheit(val)
            k_val = converter.to_kelvin(val)
            print(f"{val}°C -> {f_val:.2f}°F, {k_val:.2f}K")
        except Exception as e:
            print(f"Error converting {val}: {e}")
    fahrenheit_values = [32, 212]
    print("\nCelsius to Kelvin (via F):")
    for val in fahrenheit_values:
        try:
            c_val = converter.to_celsius(val)
            k_val = converter.to_kelvin(c_val)
            print(f"{val}°F -> {c_val:.2f}°C, {k_val:.2f}K")
        except Exception as e:
            print(f"Error converting {val}: {e}")
    kelvin_values = [273.15, 373.15]
    print("\nCelsius to Fahrenheit (via K):")
    for val in kelvin_values:
        try:
            c_val = converter.to_celsius_from_kelvin(val)
            f_val = converter.to_fahrenheit(c_val)
            print(f"{val}K -> {c_val:.2f}°C, {f_val:.2f}°F")
        except Exception as e:
            print(f"Error converting {val}: {e}")
    print("\nTesting Invalid Input:")
    try:
        converter.to_fahrenheit("invalid")
    except TypeError as te:
        print(f"Caught expected error for string input: {te}")