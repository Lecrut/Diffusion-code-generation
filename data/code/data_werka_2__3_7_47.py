class TemperatureConverter:
    FAHRENHEIT_FACTOR = 9 / 5
    FAHRENHEIT_OFFSET = 32

    def convert_all(self, celsius_readings):
        return [(c * self.FAHRENHEIT_FACTOR) + self.FAHRENHEIT_OFFSET for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [15, 20, -10, 30]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)