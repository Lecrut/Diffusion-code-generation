class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def convert_all(self, celsius_readings):
        return [self.convert_celsius_to_fahrenheit(c) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_temperatures = [0, 100, -40, 37]
    converted_temperatures = converter.convert_all(sample_temperatures)
    print(converted_temperatures)