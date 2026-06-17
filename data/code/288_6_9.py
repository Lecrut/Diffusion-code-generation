class TemperatureConverter:
    def __init__(self):
        self.conversion_factors = {
            "Celsius_to_Fahrenheit": 9/5,
            "Fahrenheit_to_Celsius": 5/9,
            "Celsius_to_Kelvin": 1,
            "Kelvin_to_Celsius": 1,
            "Fahrenheit_to_Kelvin": 5/9 + 273.15,
            "Kelvin_to_Fahrenheit": (5/9 - 273.15)
        }
    def convert(self, value, from_scale, to_scale):
        if from_scale == to_scale:
            return value
        if from_scale == "Celsius":
            if to_scale == "Fahrenheit":
                return value * (9/5) + 32
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
    print("--- Testing Conversions ---")
    celsius_temp = 20.0
    fahrenheit = converter.convert(celsius_temp, "Celsius", "Fahrenheit")
    print(f"{celsius_temp}°C is {fahrenheit:.2f}°F")
    fahrenheit_temp = 68.0
    celsius = converter.convert(fahrenheit_temp, "Fahrenheit", "Celsius")
    print(f"{fahrenheit_temp}°F is {celsius:.2f}°C")
    celsius_to_kelvin = 100.0
    kelvin = converter.convert(celsius_to_kelvin, "Celsius", "Kelvin")
    print(f"{celsius_to_kelvin}°C is {kelvin:.2f}K")
    kelvin_to_celsius = 300.15
    celsius_from_kelvin = converter.convert(kelvin_to_celsius, "Kelvin", "Celsius")
    print(f"{kelvin_to_celsius}K is {celsius_from_kelvin:.2f}°C")
    fahrenheit_to_kelvin = 32.0
    kelvin_from_fahrenheit = converter.convert(fahrenheit_to_kelvin, "Fahrenheit", "Kelvin")
    print(f"{fahrenheit_to_kelvin}°F is {kelvin_from_fahrenheit:.2f}K")
    kelvin_to_fahrenheit = 300.15
    fahrenheit_from_kelvin = converter.convert(kelvin_to_fahrenheit, "Kelvin", "Fahrenheit")
    print(f"{kelvin_to_fahrenheit}K is {fahrenheit_from_kelvin:.2f}°F")