class TemperatureConverter:
    def __init__(self):
        self._fahrenheit_to_kelvin_factor = 5 / 9
        self._kelvin_offset = 273.15

    def fahrenheit_to_kelvin(self, fahrenheit):
        return (fahrenheit - 32) * self._fahrenheit_to_kelvin_factor + self._kelvin_offset

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_values = [0, 50, 77, 100]
    for value in sample_values:
        kelvin_value = converter.fahrenheit_to_kelvin(value)
        print(f"{value} Fahrenheit is {kelvin_value:.2f} Kelvin")