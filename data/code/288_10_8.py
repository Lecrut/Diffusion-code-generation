class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 // 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 // 9

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = 25
    print("Celsius to Fahrenheit:", converter.celsius_to_fahrenheit(sample_celsius))
    sample_fahrenheit = 77
    print("Fahrenheit to Celsius:", converter.fahrenheit_to_celsius(sample_fahrenheit))