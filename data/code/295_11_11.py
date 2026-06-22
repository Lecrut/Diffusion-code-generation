class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    converter = TemperatureConverter()
    temp_celsius = 25.0
    temp_fahrenheit = converter.celsius_to_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C is {temp_fahrenheit:.1f}°F")
    
    temp_fahrenheit = 77.0
    temp_celsius = converter.fahrenheit_to_celsius(temp_fahrenheit)
    print(f"{temp_fahrenheit}°F is {temp_celsius:.1f}°C")