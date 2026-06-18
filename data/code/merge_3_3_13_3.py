class TemperatureConverter:
    def convert_all(self, celsius_readings):
        """Converts a list of Celsius temperatures to Fahrenheit."""
        return [c * 9 / 5 + 32 for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celcius = [-40, -10, 0, 25, 100]
    fahrenheit_results = converter.convert_all(sample_celcius)
    print(f"Celsius to Fahrenheit conversion results: {fahrenheit_results}")