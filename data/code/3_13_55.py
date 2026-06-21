class TemperatureConverter:
    def __init__(self, fahrenheit_temperatures):
        self.fahrenheit_temperatures = fahrenheit_temperatures

    def convert_to_celsius(self):
        conversion_factor = 5 / 9
        offset = 32
        return tuple(map(lambda f: (f - offset) * conversion_factor, self.fahrenheit_temperatures))

if __name__ == '__main__':
    sample_temperatures = (45, 86, 130, 374)
    converter = TemperatureConverter(sample_temperatures)
    celsius_temperatures = converter.convert_to_celsius()
    print(celsius_temperatures)