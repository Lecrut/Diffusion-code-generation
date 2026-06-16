class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return (celsius * 9/5) + 32
    def fahrenheit_to_celsius(self, fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Input must be a number.")
        return (fahrenheit - 32) * 5/9
    def celsius_to_kelvin(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return celsius + 273.15
    def kelvin_to_celsius(self, kelvin):
        if not isinstance(kelvin, (int, float)):
            raise TypeError("Input must be a number.")
        return kelvin - 273.15
    def fahrenheit_to_kelvin(self, fahrenheit):
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        return self.celsius_to_kelvin(celsius)
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_sample = 25.0
    fahrenheit_sample = 77.0
    kelvin_sample = 298.15
    print(f"Celsius to Fahrenheit: {converter.celsius_to_fahrenheit(celsius_sample):.2f}")
    print(f"Fahrenheit to Celsius: {converter.fahrenheit_to_celsius(fahrenheit_sample):.2f}")
    print(f"Celsius to Kelvin: {converter.celsius_to_kelvin(celsius_sample):.2f}")
    print(f"Kelvin to Celsius: {converter.kelvin_to_celsius(kelvin_sample):.2f}")
    print(f"Fahrenheit to Kelvin: {converter.fahrenheit_to_kelvin(fahrenheit_sample):.2f}")
    try:
        converter.celsius_to_fahrenheit("invalid")
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        converter.celsius_to_kelvin(300.5)
    except Exception as e:
        print(f"Unexpected error: {e}")