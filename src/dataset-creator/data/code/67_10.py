from typing import Optional
class TemperatureConverter:
    def celsius_to_fahrenheit(self, temperature_celsius: float) -> float:
        return (temperature_celsius * 9 / 5) + 32
    def fahrenheit_to_celsius(self, temperature_fahrenheit: float) -> float:
        return (temperature_fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    celsius_samples: list[float] = [0, 100, -40, 25.5]
    converter = TemperatureConverter()
    print("Celsius to Fahrenheit Conversion:")
    for temp_c in celsius_samples:
        temp_f = converter.celsius_to_fahrenheit(temp_c)
        print(f"{temp_c}°C -> {temp_f:.1f}°F")
    print("\nFahrenheit to Celsius Conversion:")
    fahrenheit_samples: list[float] = [32, 212, -40, 68.75]
    for temp_f in fahrenheit_samples:
        temp_c = converter.fahrenheit_to_celsius(temp_f)
        print(f"{temp_f}°F -> {temp_c:.1f}°C")