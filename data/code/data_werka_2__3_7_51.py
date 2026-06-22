class TemperatureConverter:
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
    FAHRENHEIT_OFFSET = 32

    def convert_all(self, celsius_readings):
        return [self._convert(c) for c in celsius_readings]

    def _convert(self, celsius):
        return (celsius * self.CELSIUS_TO_FAHRENHEIT_FACTOR) + self.FAHRENHEIT_OFFSET

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [-40, 0, 25, 100]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)