class TemperatureConverter:
    def convert_all(self, celsius_readings):
        def celsius_to_fahrenheit(c):
            return c * 9.0 / 5.0 + 32.0

        return [celsius_to_fahrenheit(c) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [0, 100, 37, -40, 25]
    fahrenheit_results = converter.convert_all(sample_celsius)
    print(fahrenheit_results)