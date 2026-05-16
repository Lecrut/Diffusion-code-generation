class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_temp = 25.0
    fahrenheit_temp = converter.celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")