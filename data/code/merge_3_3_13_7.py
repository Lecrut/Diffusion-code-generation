class TemperatureConverter:
    def convert_all(self, celsius_readings):
        """Converts a list of Celsius temperatures to Fahrenheit."""
        fahrenheit = [c * 9 / 5 + 32 for c in celsius_readings]
        return fahrenheit

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [-40, -10, 0, 25, 100]
    result = converter.convert_all(sample_celsius)
    print("Celsius:", sample_celsius)
    print("Fahrenheit:", result)