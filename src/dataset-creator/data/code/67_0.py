class TemperatureConverter:
    def to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return (celsius * 9 / 5) + 32
    def to_kelvin(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise TypeError("Input must be a number.")
        return celsius + 273.15
    def to_celsius(self, fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            raise TypeError("Input must be a number.")
        return (fahrenheit - 32) * 5 / 9
    def to_fahrenheit_from_kelvin(self, kelvin):
        if not isinstance(kelvin, (int, float)):
            raise TypeError("Input must be a number.")
        return (kelvin - 273.15) * 9 / 5 + 32
    def to_celsius_from_kelvin(self, kelvin):
        if not isinstance(kelvin, (int, float)):
            raise TypeError("Input must be a number.")
        return kelvin - 273.15
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_value = 0
    fahrenheit_result = converter.to_fahrenheit(celsius_value)
    kelvin_result = converter.to_kelvin(celsius_value)
    print(f"{celsius_value}°C is {fahrenheit_result:.2f}°F")
    print(f"{celsius_value}°C is {kelvin_result:.2f}K")
    fahrenheit_value = 32.0
    celsius_from_f = converter.to_celsius(fahrenheit_value)
    kelvin_from_f = (fahrenheit_value - 32) * 5 / 9 + 273.15
    print(f"{fahrenheit_value}°F is {celsius_from_f:.2f}°C")
    print(f"{fahrenheit_value}°F is {kelvin_from_f:.2f}K")
    kelvin_value = 373.15
    celsius_from_k = converter.to_celsius_from_kelvin(kelvin_value)
    fahrenheit_from_k = (kelvin_value - 273.15) * 9 / 5 + 32
    print(f"{kelvin_value}K is {celsius_from_k:.2f}°C")
    print(f"{kelvin_value}K is {fahrenheit_from_k:.2f}°F")