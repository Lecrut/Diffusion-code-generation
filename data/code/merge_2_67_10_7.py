from typing import Optional
class TemperatureConverter:
    def to_fahrenheit(self, celsius: float) -> float:
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be an integer or float.")
        return celsius * 9 / 5 + 32
    def to_celsius(self, fahrenheit: float) -> float:
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Input must be an integer or float.")
        return (fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_samples: list[float] = [0, 10.5, -40, 100]
    fahrenheit_samples: list[float] = [-40, 68.7, 32, 212]
    print("Celsius to Fahrenheit conversions:")
    for c in celsius_samples:
        result_f = converter.to_fahrenheit(c)
        print(f"{c}°C -> {result_f:.2f}°F")
    print("\nFahrenheit to Celsius conversions:")
    for f in fahrenheit_samples:
        result_c = converter.to_celsius(f)
        print(f"{f}°F -> {result_c:.2f}°C")