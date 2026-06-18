from typing import Optional
class TemperatureConverter:
    def to_fahrenheit(self, celsius: float) -> float:
        return (celsius * 9 / 5) + 32
    def to_celsius(self, fahrenheit: float) -> float:
        return ((fahrenheit - 32) * 5 / 9)
    def convert(self, value: float, from_unit: str, to_unit: str) -> Optional[float]:
        if from_unit.upper() == "C" and to_unit.upper() == "F":
            return self.to_fahrenheit(value)
        elif from_unit.upper() == "F" and to_unit.upper() == "C":
            return self.to_celsius(value)
        else:
            raise ValueError("Unsupported conversion direction. Supported pairs are C->F or F->C.")
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_values = [0, 18, -40]
    fahrenheit_values = [32, 65.73, -40]
    print("Celsius to Fahrenheit Conversion:")
    for val in celsius_values:
        result_f = converter.to_fahrenheit(val)
        print(f"{val}°C -> {result_f:.2f}°F")
    print("\nFahrenheit to Celsius Conversion:")
    for val in fahrenheit_values:
        result_c = converter.to_celsius(val)
        print(f"{val}°F -> {result_c:.2f}°C")
    test_cases = [
        (0, 'C', 'F'),
        (-40, 'F', 'C'),
        (18.36, 'C', 'F')                               
    ]
    print("\nMixed Conversion Tests:")
    for value, from_unit, to_unit in test_cases:
        try:
            converted = converter.convert(value, from_unit.lower(), to_unit.lower())
            original_label = "Celsius" if from_unit == 'C' else "Fahrenheit"
            target_label = "Fahrenheit" if to_unit == 'F' else "Celsius"
            print(f"{value}°{original_label.upper()} -> {converted:.2f}°{target_label}")
        except ValueError as e:
            print(f"Error converting from {from_unit} to {to_unit}: {e}")