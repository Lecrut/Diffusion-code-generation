class TemperatureConverter:
    def __init__(self):
        self.conversion_factor = 9 / 5
        self.offset = 32

    def convert(self, celsius):
        return (celsius * self.conversion_factor) + self.offset

    def convert_all(self, celsius_readings):
        if not all(isinstance(c, (int, float)) for c in celsius_readings):
            raise ValueError("All elements in the list must be numbers.")
        return [self.convert(c) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [-20, -10, 0, 10, 20]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)