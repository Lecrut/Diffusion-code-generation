class TemperatureConverter:
    def __init__(self):
        self.conversion_factor = 9 / 5
        self.base_temperature = 32

    def celsius_to_fahrenheit(self, celsius_list):
        return [c * self.conversion_factor + self.base_temperature for c in celsius_list]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_temperatures = [-40, 0, 100, 37]
    fahrenheit_temperatures = converter.celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)