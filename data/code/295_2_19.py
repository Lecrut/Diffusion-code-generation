class TemperatureConverter:
    FAHRENHEIT_TO_CELSIUS = 5 / 9
    OFFSET = -32

    @staticmethod
    def convert_fahrenheit_to_celsius(fahrenheit):
        return int((fahrenheit + TemperatureConverter.OFFSET) * TemperatureConverter.FAHRENHEIT_TO_CELSIUS)
if __name__ == '__main__':
    converter = TemperatureConverter()
    print(converter.convert_fahrenheit_to_celsius(32))
    print(converter.convert_fahrenheit_to_celsius(212))