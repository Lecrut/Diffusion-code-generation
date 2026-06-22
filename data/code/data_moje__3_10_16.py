class TemperatureConverter:
    def convert_all(self, celsius_readings):
        return [c * 9 / 5 + 32 for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    readings = [0, 25, 37, 100]
    result = converter.convert_all(readings)
    print(result)