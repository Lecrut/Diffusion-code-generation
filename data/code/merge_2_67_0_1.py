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
if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_values = [0, 100, -40]
    for temp in celsius_values:
        fahrenheit_temp = converter.to_fahrenheit(temp)
        kelvin_temp = converter.to_kelvin(temp)
        print(f"{temp}°C is {fahrenheit_temp:.2f}°F and {kelvin_temp:.2f}K")