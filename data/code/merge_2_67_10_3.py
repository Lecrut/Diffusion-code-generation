from typing import Optional
class TemperatureConverter:
    def to_fahrenheit(self, celsius: float) -> float:
        return celsius * 9 / 5 + 32
    def to_celsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5 / 9
if __name__ == '__main__':
    converter = TemperatureConverter()
    c_to_f_samples: list[tuple[float, float]] = [
        (-40.0, -40.0),
        (0.0, 32.0),
        (15.0, 59.0),
        (100.0, 212.0)
    ]
    f_to_c_samples: list[tuple[float, float]] = [
        (-40.0, -40.0),
        (32.0, 0.0),
        (59.0, 15.0),
        (212.0, 100.0)
    ]
    print("Celsius to Fahrenheit conversions:")
    for c_val, expected_f in c_to_f_samples:
        result = converter.to_fahrenheit(c_val)
        assert abs(result - expected_f) < 0.0001, f"Conversion failed for {c_val}"
        print(f"{c_val}°C -> {result:.2f}°F")
    print("\nFahrenheit to Celsius conversions:")
    for f_val, expected_c in f_to_c_samples:
        result = converter.to_celsius(f_val)
        assert abs(result - expected_c) < 0.0001, f"Conversion failed for {f_val}"
        print(f"{f_val}°F -> {result:.2f}°C")
    test_values: list[float] = [-50.0, -10.0, 0.0, 10.0, 37.5, 86.0, 90.0, 200.0]
    print("\nRound-trip conversion verification:")
    for val in test_values:
        celsius = converter.to_celsius(val)
        back_to_fahrenheit = converter.to_fahrenheit(celsius)
        assert abs(back_to_fahrenheit - val) < 1e-9, f"Round-trip failed for {val}"
    print("All conversions verified successfully.")