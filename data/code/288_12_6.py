class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_value = 25.0
    fahrenheit_result = converter.celsius_to_fahrenheit(celsius_value)
    print(f"{celsius_value}°C is {fahrenheit_result}°F")
    fahrenheit_value = 77.0
    celsius_result = converter.fahrenheit_to_celsius(fahrenheit_value)
    print(f"{fahrenheit_value}°F is {celsius_result}°C")
    kelvin_value = 300.0
    celsius_from_kelvin = converter.kelvin_to_celsius(kelvin_value)
    print(f"{kelvin_value}K is {celsius_from_kelvin}°C")