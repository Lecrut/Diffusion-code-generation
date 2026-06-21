class TemperatureConverter:
    def __init__(self):
        self.conversion_factor = 9 / 5
        self.offset = 32

    def celsius_to_fahrenheit(self, celsius_list):
        return [(c * self.conversion_factor) + self.offset for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, 0, 100, 37]
    converter = TemperatureConverter()
    fahrenheit_temperatures = converter.celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)