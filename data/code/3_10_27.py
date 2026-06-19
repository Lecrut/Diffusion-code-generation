class TemperatureConverter:
    def convert_all(self, celsius_readings):
        return [self.celsius_to_fahrenheit(c) for c in celsius_readings]

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius_temps = [0, 10, 20, 30, 40]
    fahrenheit_temps = converter.convert_all(sample_celsius_temps)
    print(fahrenheit_temps)