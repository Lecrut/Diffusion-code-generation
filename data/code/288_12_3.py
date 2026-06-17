class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_temp = 25.0
    fahrenheit_temp = converter.celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is {fahrenheit_temp}°F")
    fahrenheit_sample = 68.0
    celsius_from_fahrenheit = converter.fahrenheit_to_celsius(fahrenheit_sample)
    print(f"{fahrenheit_sample}°F is {celsius_from_fahrenheit}°C")
    kelvin_temp = 300.0
    celsius_from_kelvin = converter.kelvin_to_celsius(kelvin_temp)
    print(f"{kelvin_temp}K is {celsius_from_kelvin}°C")