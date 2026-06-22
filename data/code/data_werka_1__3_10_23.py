class TemperatureConverter:
    def convert_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def convert_all(self, celsius_readings):
        return [self.convert_to_fahrenheit(c) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius_readings = [0, 10, 20, 30, 40]
    fahrenheit_readings = converter.convert_all(sample_celsius_readings)
    print(fahrenheit_readings)