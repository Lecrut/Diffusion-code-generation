class TemperatureConverter:
    def convert_all(self, celsius_readings):
        fahrenheit_readings = []
        for c in celsius_readings:
            f = (c * 9 / 5) + 32
            fahrenheit_readings.append(f)
        return fahrenheit_readings

if __name__ == '__main__':
    converter = TemperatureConverter()
    readings = [0, 100, 36.6]
    results = converter.convert_all(readings)
    print(results)