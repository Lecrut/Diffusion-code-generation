class TemperatureConverter:
    FAHRENHEIT_FACTOR = 9 / 5
    FAHRENHEIT_OFFSET = 32

    def convert_all(self, celsius_readings):
        return [self._convert_to_fahrenheit(c) for c in celsius_readings]

    def _convert_to_fahrenheit(self, celsius):
        return (celsius * self.FAHRENHEIT_FACTOR) + self.FAHRENHEIT_OFFSET

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [15, 25, 35, -10]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)