class TemperatureConverter:
    def __init__(self):
        self.factor = 9 / 5
        self.offset = 32

    def convert(self, celsius):
        return (celsius * self.factor) + self.offset

    def convert_all(self, celsius_readings):
        if not isinstance(celsius_readings, list):
            raise ValueError("Input must be a list of Celsius temperatures.")
        return [self.convert(c) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [-40, 0, 100, 37.5]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)