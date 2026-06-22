class TemperatureConverter:
    def convert_all(self, celsius_readings):
        return [(c * 9.0 / 5.0) + 32 for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_values = [0, 25, 37.5, 100]
    fahrenheit_values = converter.convert_all(celsius_values)
    print(fahrenheit_values)