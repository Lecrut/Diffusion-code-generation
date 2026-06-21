class TemperatureConverter:
    def __init__(self):
        self.conversion_factor = 9 / 5
        self.offset = 32

    def convert_single(self, celsius):
        return (celsius * self.conversion_factor) + self.offset

    def convert_all(self, celsius_readings):
        fahrenheit_readings = []
        for celsius in celsius_readings:
            fahrenheit = self.convert_single(celsius)
            fahrenheit_readings.append(fahrenheit)
        return fahrenheit_readings

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [15, 20, 30, -10]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)