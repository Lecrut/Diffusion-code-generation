class TemperatureConverter:
    def __init__(self):
        self.conversion_factor = 9 / 5
        self.freezing_point_offset = 32

    def convert_celsius_to_fahrenheit(self, celsius):
        return (celsius * self.conversion_factor) + self.freezing_point_offset

    def convert_all(self, celsius_readings):
        fahrenheit_readings = []
        for temperature in celsius_readings:
            fahrenheit = self.convert_celsius_to_fahrenheit(temperature)
            fahrenheit_readings.append(fahrenheit)
        return fahrenheit_readings

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius_temperatures = [15, 20, 30, -10]
    converted_temperatures = converter.convert_all(sample_celsius_temperatures)
    print(converted_temperatures)