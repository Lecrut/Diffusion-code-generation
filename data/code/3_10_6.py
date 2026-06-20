class TemperatureConverter:
    def convert_all(self, celsius_readings):
        return [c * 9 / 5 + 32 for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    celsius_samples = [0, 10, 25, 100]
    print(converter.convert_all(celsius_samples))