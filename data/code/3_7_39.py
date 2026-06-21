class TemperatureConverter:
    def __init__(self):
        self.celsius_to_fahrenheit_factor = 9 / 5
        self.fahrenheit_offset = 32

    def convert(self, celsius):
        return (celsius * self.celsius_to_fahrenheit_factor) + self.fahrenheit_offset

    def convert_all(self, celsius_readings):
        fahrenheit_readings = []
        for celsius in celsius_readings:
            fahrenheit = self.convert(celsius)
            fahrenheit_readings.append(fahrenheit)
        return fahrenheit_readings

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [-10, 0, 25, 50, 75]
    fahrenheit_readings = converter.convert_all(sample_celsius)
    print(fahrenheit_readings)