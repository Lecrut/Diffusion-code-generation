class TemperatureConverter:
    def convert_all(self, celsius_readings):
        return [(c * 9/5) + 32 for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius_readings = [0, 100, -40, 37]
    fahrenheit_readings = converter.convert_all(sample_celsius_readings)
    print(fahrenheit_readings)