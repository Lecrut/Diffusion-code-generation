class TemperatureConverter:
    CONVERSION_FACTOR = 9 / 5
    OFFSET = 32

    @staticmethod
    def convert_celsius_to_fahrenheit(celsius_list):
        return [(c * TemperatureConverter.CONVERSION_FACTOR) + TemperatureConverter.OFFSET for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, -10, 0, 25, 100]
    converter = TemperatureConverter()
    fahrenheit_temperatures = converter.convert_celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)