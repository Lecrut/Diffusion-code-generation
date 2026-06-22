class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9

if __name__ == '__main__':
    print(TemperatureConverter.celsius_to_fahrenheit(0))
    print(TemperatureConverter.fahrenheit_to_celsius(32))