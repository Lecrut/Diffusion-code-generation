class TemperatureConverter:
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
    FAHRENHEIT_OFFSET = 32

    @staticmethod
    def convert_to_celsius(fahrenheit):
        return tuple(map(lambda f: (f - TemperatureConverter.FAHRENHEIT_OFFSET) * TemperatureConverter.FAHRENHEIT_TO_CELSIUS_FACTOR, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (50, 72, 98.6, 320)
    celsius_temperatures = TemperatureConverter.convert_to_celsius(sample_temperatures)
    print(celsius_temperatures)