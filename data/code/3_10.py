class TemperatureConverter:
    def convert_all(self, celsius_readings):
        return [c * 9 / 5 + 32 for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_values = [0, 100, 37, 25]
    fahrenheit_values = converter.convert_all(celsius_values)
    print(fahrenheit_values)