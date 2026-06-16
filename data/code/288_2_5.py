class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        return (celsius * 9/5) + 32
    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5/9
    def celsius_to_kelvin(self, celsius: float) -> float:
        return celsius + 273.15
    def kelvin_to_celsius(self, kelvin: float) -> float:
        return kelvin - 273.15
    def fahrenheit_to_kelvin(self, fahrenheit: float) -> float:
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        return self.celsius_to_kelvin(celsius)
    def kelvin_to_fahrenheit(self, kelvin: float) -> float:
        celsius = self.kelvin_to_celsius(kelvin)
        return self.celsius_to_fahrenheit(celsius)
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_value = 25.0
    fahrenheit_value = 77.0
    kelvin_value = 298.15
    print(f"Celsius to Fahrenheit: {converter.celsius_to_fahrenheit(celsius_value):.2f}")
    print(f"Fahrenheit to Celsius: {converter.fahrenheit_to_celsius(fahrenheit_value):.2f}")
    print(f"Celsius to Kelvin: {converter.celsius_to_kelvin(celsius_value):.2f}")
    print("-" * 20)
    print(f"Fahrenheit to Kelvin: {converter.fahrenheit_to_kelvin(fahrenheit_value):.2f}")
    print(f"Kelvin to Fahrenheit: {converter.kelvin_to_fahrenheit(kelvin_value):.2f}")