class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = 0
    print(f"Fahrenheit: {converter.celsius_to_fahrenheit(sample_celsius)}")
    sample_celsius_2 = 100
    print(f"Fahrenheit: {converter.celsius_to_fahrenheit(sample_celsius_2)}")