class TemperatureConverter:

    def convert_fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return int(celsius)
if __name__ == '__main__':
    converter = TemperatureConverter()
    print(converter.convert_fahrenheit_to_celsius(32))
    print(converter.convert_fahrenheit_to_celsius(212))
    print(converter.convert_fahrenheit_to_celsius(-40))