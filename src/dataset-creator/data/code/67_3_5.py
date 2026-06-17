import math
class TemperatureConverter:
    def to_celsius(self, temperature):
        return (temperature - 32) * 5 / 9
    def to_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32
    def to_kelvin(self, celsius):
        return celsius + 273.15
    def to_celsius_from_kelvin(self, kelvin):
        return kelvin - 273.15
def convert_temperature(value, from_scale, to_scale):
    converter = TemperatureConverter()
    if from_scale == 'F':
        value = converter.to_fahrenheit(value)
    elif from_scale == 'C':
        pass
    elif from_scale == 'K':
        value = converter.to_celsius_from_kelvin(value)
    else:
        raise ValueError("Invalid source scale")
    if to_scale == 'F':
        return round(converter.to_fahrenheit(value), 2)
    elif to_scale == 'C':
        return round(converter.to_celsius(value), 2)
    elif to_scale == 'K':
        return round(converter.to_kelvin(value), 2)
if __name__ == '__main__':
    test_cases = [
        (100, "F", "C"),
        (-40, "C", "F"),
        (37.8, "K", "C"),
        (98.6, "F", "K")
    ]
    for value, from_s, to_s in test_cases:
        result = convert_temperature(value, from_s, to_s)
        print(f"{value} {from_s} is equal to {result} {to_s}")