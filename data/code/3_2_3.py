class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_value = 25.0
    fahrenheit_value = converter.celsius_to_fahrenheit(celsius_value)
    print(f"{celsius_value}°C is equal to {fahrenheit_value}°F")