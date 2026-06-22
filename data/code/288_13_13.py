class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

if __name__ == '__main__':
    converter = TemperatureConverter()
    temperatures_celsius = [0, 10, 20, 30, 40]
    temperatures_fahrenheit = [converter.celsius_to_fahrenheit(c) for c in temperatures_celsius]
    print(temperatures_fahrenheit)