class TemperatureConverter:
    FAHRENHEIT_TO_CELSIUS_OFFSET = 32
    FAHRENHEIT_TO_CELSIUS_MULTIPLIER = 5 / 9

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - TemperatureConverter.FAHRENHEIT_TO_CELSIUS_OFFSET) * TemperatureConverter.FAHRENHEIT_TO_CELSIUS_MULTIPLIER
        return int(round(celsius))
if __name__ == '__main__':
    converter = TemperatureConverter()
    print(converter.fahrenheit_to_celsius(32))
    print(converter.fahrenheit_to_celsius(212))
    print(converter.fahrenheit_to_celsius(98.6))