from typing import Optional
class TemperatureConverter:
    def to_fahrenheit(self, celsius: float) -> float:
        return (celsius * 9 / 5) + 32
    def to_celsius(self, fahrenheit: float) -> float:
        return ((fahrenheit - 32) * 5 / 9)
if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius_values = [0, 18, 37.6]
    sample_fahrenheit_values = [32, 66, 99.68]
    print("Celsius to Fahrenheit:")
    for c in sample_celsius_values:
        f = converter.to_fahrenheit(c)
        print(f"{c}°C -> {f:.2f}°F")
    print("\nFahrenheit to Celsius:")
    for f in sample_fahrenheit_values:
        c = converter.to_celsius(f)
        print(f"{f}°F -> {c:.2f}°C")
    original_temp = 10.5
    converted_back = converter.to_celsius(converter.to_fahrenheit(original_temp))
    assert abs(converted_back - original_temp) < 0.001, "Round-trip conversion failed"