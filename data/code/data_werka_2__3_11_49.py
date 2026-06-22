class TemperatureConverter:
    def __init__(self):
        self.factor = 9 / 5
        self.offset = 32

    def convert(self, celsius_list):
        return [self._convert_single(c) for c in celsius_list]

    def _convert_single(self, temp):
        if not isinstance(temp, (int, float)):
            raise ValueError("Temperature must be an integer or float.")
        return temp * self.factor + self.offset

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_temperatures = [0, 100, -40, 37]
    fahrenheit_temperatures = converter.convert(sample_temperatures)
    print(fahrenheit_temperatures)

    try:
        invalid_temperature = "not a number"
        result = converter._convert_single(invalid_temperature)
        print(result)
    except ValueError as e:
        print(e)