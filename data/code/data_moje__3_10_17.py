class TemperatureConverter:
    def __init__(self):
        self._conversion_rate = 9 / 5
        self._offset = 32

    def celsius_to_fahrenheit(self, celsius):
        return celsius * self._conversion_rate + self._offset

    def convert_all(self, celsius_readings):
        return [self.celsius_to_fahrenheit(c) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [0, 10, 20, 30, 100]
    fahrenheit_results = converter.convert_all(sample_celsius)
    print(fahrenheit_results)