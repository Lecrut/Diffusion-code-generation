class TemperatureConverter:
    def convert_all(self, celsius_readings):
        return [(c * 9 / 5) + 32 for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = [0, 25, 100, -40]
    print(converter.convert_all(sample_celsius))