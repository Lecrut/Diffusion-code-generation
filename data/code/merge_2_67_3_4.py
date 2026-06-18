import math
class TemperatureConverter:
    def to_celsius(self, value):
        return (value - 32) * 5 / 9
    def to_fahrenheit(self, celsius_value):
        return celsius_value * 9 / 5 + 32
    def to_kelvin(self, celsius_value):
        return celsius_value + 273.15
    def to_celsius_from_kelvin(self, kelvin_value):
        return kelvin_value - 273.15
def convert_temperature(value: float, from_scale: str, to_scale: str) -> tuple[float, dict]:
    converter = TemperatureConverter()
    if from_scale == 'C':
        celsius = value
    elif from_scale == 'F':
        celsius = converter.to_celsius(value)
    elif from_scale == 'K':
        celsius = converter.to_celsius_from_kelvin(value)
    else:
        raise ValueError("Unsupported source scale")
    if to_scale == 'C':
        result = celsius
    elif to_scale == 'F':
        result = converter.to_fahrenheit(celsius)
    elif to_scale == 'K':
        result = converter.to_kelvin(celsius)
    else:
        raise ValueError("Unsupported target scale")
    history = {from_scale: value, "C": celsius}
    if from_scale != 'C' and to_scale != 'C':
        history["F"] = converter.to_fahrenheit(value)
    return result, history
if __name__ == '__main__':
    test_cases = [
        (0, 'C', 'F'),
        (100, 'C', 'K'),
        (-40, 'F', 'C'),
        (273.15, 'K', 'C')
    ]
    for value, from_s, to_s in test_cases:
        result, history = convert_temperature(value, from_s, to_s)
        print(f"Converting {value}°{from_s} to °{to_s}: Result is {result}")