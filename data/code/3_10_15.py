class TemperatureConverter:
    def convert_all(self, celsius_readings):
        return [c * 9 / 5 + 32 for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    print(converter.convert_all([0, 100, 37, -40]))