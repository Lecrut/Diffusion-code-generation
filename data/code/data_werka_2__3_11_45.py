class TemperatureConverter:
    def __init__(self):
        self.factor = 9 / 5
        self.offset = 32

    def convert_celsius_to_fahrenheit(self, celsius_list):
        return [c * self.factor + self.offset for c in celsius_list]

    def display_conversions(self, celsius_list):
        fahrenheit_list = self.convert_celsius_to_fahrenheit(celsius_list)
        for c, f in zip(celsius_list, fahrenheit_list):
            print(f"{c}°C is {f}°F")

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_temperatures = [30, -10, 25, 100]
    converter.display_conversions(sample_temperatures)