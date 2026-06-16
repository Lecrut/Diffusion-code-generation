import math
class TemperatureConverter:
    def __init__(self):
        self.conversion_factors = {
            "Celsius_to_Fahrenheit": 1.8,
            "Celsius_to_Kelvin": 1.0,
            "Fahrenheit_to_Celsius": 5/9,
            "Fahrenheit_to_Kelvin": 5/9 + 273.15,
            "Kelvin_to_Celsius": -273.15,
        }
    def convert(self, value, from_scale, to_scale):
        if from_scale == to_scale:
            return value
        if from_scale == "Celsius":
            if to_scale == "Fahrenheit":
                return value * 1.8 + 32
            elif to_scale == "Kelvin":
                return value + 273.15
        elif from_scale == "Fahrenheit":
            if to_scale == "Celsius":
                return (value - 32) * (5/9)
            elif to_scale == "Kelvin":
                return (value - 32) * (5/9) + 273.15
        elif from_scale == "Kelvin":
            if to_scale == "Celsius":
                return value - 273.15
            elif to_scale == "Fahrenheit":
                return (value - 273.15) * (9/5) + 32
        raise ValueError("Invalid conversion requested")
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_temp = 20.0
    fahrenheit_temp = 68.0
    kelvin_temp = 293.15
    print(f"Celsius to Fahrenheit: {converter.convert(celsius_temp, 'Celsius', 'Fahrenheit'):.2f}")
    print(f"Celsius to Kelvin: {converter.convert(celsius_temp, 'Celsius', 'Kelvin'):.2f}")
    print("-" * 20)
    print(f"Fahrenheit to Celsius: {converter.convert(fahrenheit_temp, 'Fahrenheit', 'Celsius'):.2f}")
    print(f"Fahrenheit to Kelvin: {converter.convert(fahrenheit_temp, 'Fahrenheit', 'Kelvin'):.2f}")
    print("-" * 20)
    print(f"Kelvin to Celsius: {converter.convert(kelvin_temp, 'Kelvin', 'Celsius'):.2f}")
    print(f"Kelvin to Fahrenheit: {converter.convert(kelvin_temp, 'Kelvin', 'Fahrenheit'):.2f}")