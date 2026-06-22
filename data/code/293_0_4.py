class TemperatureConverter:
    def celsius_to_fahrenheit(self, c):
        return c * 9 / 5 + 32
    
    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5 / 9

if __name__ == '__main__':
    converter = TemperatureConverter()
    print(converter.celsius_to_fahrenheit(0))
    print(converter.fahrenheit_to_celsius(32))