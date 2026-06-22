class TemperatureConverter:
    def __init__(self):
        self.offset = 273.15

    def celsius_to_kelvin(self, celsius):
        return celsius + self.offset

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_values = [0, -40, 100, 37]
    for value in sample_values:
        print(f"{value}C is {converter.celsius_to_kelvin(value)}K")