class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9//5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5//9

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = 25
    sample_fahrenheit = 77
    
    print(f"Celsius to Fahrenheit: {converter.celsius_to_fahrenheit(sample_celsius)}")
    print(f"Fahrenheit to Celsius: {converter.fahrenheit_to_celsius(sample_fahrenheit)}")