class TemperatureConverter:
    def convert_all(self, celsius_readings):
        return [(c * 9/5) + 32 for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius_temps = [0, 100, -40, 37]
    fahrenheit_temps = converter.convert_all(sample_celsius_temps)
    print(fahrenheit_temps)