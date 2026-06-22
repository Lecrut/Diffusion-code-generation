class TemperatureConverter:
    def __init__(self, temperatures):
        self.temperatures = temperatures

    def find_max_temperature_celsius(self):
        return max(self.temperatures)

    def convert_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

if __name__ == '__main__':
    converter = TemperatureConverter([20, 25, 15, 30, -5])
    max_celsius = converter.find_max_temperature_celsius()
    max_fahrenheit = converter.convert_to_fahrenheit(max_celsius)
    print(f"Maximum temperature in Celsius: {max_celsius}")
    print(f"Maximum temperature in Fahrenheit: {max_fahrenheit}")