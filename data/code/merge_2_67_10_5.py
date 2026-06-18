from typing import Optional
class TemperatureConverter:
    def celsius_to_fahrenheit(self, temperature_celsius: float) -> float:
        if not isinstance(temperature_celsius, (int, float)):
            raise TypeError("Input must be an integer or float.")
        return (temperature_celsius * 9 / 5) + 32
    def fahrenheit_to_celsius(self, temperature_fahrenheit: float) -> float:
        if not isinstance(temperature_fahrenheit, (int, float)):
            raise TypeError("Input must be an integer or float.")
        return (temperature_fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_samples: list[float] = [0.0, 18.6, 40.7, -40.0]
    print("Celsius to Fahrenheit Conversion:")
    for temp_c in celsius_samples:
        result_f = converter.celsius_to_fahrenheit(temp_c)
        print(f"{temp_c:.2f}°C -> {result_f:.2f}°F")
    fahrenheit_samples: list[float] = [32.0, 68.0, 104.5, -40.0]
    print("\nFahrenheit to Celsius Conversion:")
    for temp_f in fahrenheit_samples:
        result_c = converter.fahrenheit_to_celsius(temp_f)
        print(f"{temp_f:.2f}°F -> {result_c:.2f}°C")