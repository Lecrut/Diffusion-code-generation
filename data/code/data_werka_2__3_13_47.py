class TemperatureConverter:
    FAHRENHEIT_TO_CELSIUS = lambda f: (f - 32) * 5 / 9

    @staticmethod
    def convert_temperatures(fahrenheit_tuple):
        return tuple(map(TemperatureConverter.FAHRENHEIT_TO_CELSIUS, fahrenheit_tuple))

if __name__ == '__main__':
    sample_temperatures = (45, 86, 130, 250)
    celsius_temperatures = TemperatureConverter.convert_temperatures(sample_temperatures)
    print(celsius_temperatures)