class TemperatureConverter:
    def __init__(self):
        self.factor = 9 / 5
        self.offset = 32

    def convert(self, celsius):
        return (celsius * self.factor) + self.offset

    def convert_all(self, celsius_readings):
        if not all(isinstance(c, (int, float)) for c in celsius_readings):
            raise ValueError("All elements in the list must be numeric.")
        return [self.convert(c) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius_1 = [-40, 0, 100, 37.5]
    fahrenheit_readings_1 = converter.convert_all(sample_celsius_1)
    print(fahrenheit_readings_1)

    sample_celsius_2 = [25, 30, 35, 40]
    fahrenheit_readings_2 = converter.convert_all(sample_celsius_2)
    print(fahrenheit_readings_2)