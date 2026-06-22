class TemperatureConverter:
    def convert_all(self, celsius_readings):
        return [(c, c * 9 / 5 + 32) for c in celsius_readings]

if __name__ == '__main__':
    converter = TemperatureConverter()
    readings = [0, 25, 37, 100]
    results = converter.convert_all(readings)
    for celsius, fahrenheit in results:
        print(f"{celsius} C = {fahrenheit} F")