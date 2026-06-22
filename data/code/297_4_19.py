class TemperatureConverter:

    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32
if __name__ == '__main__':
    converter = TemperatureConverter()
    print(converter.celsius_to_fahrenheit(0))
    print(converter.celsius_to_fahrenheit(100))
    print(converter.celsius_to_fahrenheit(-40))