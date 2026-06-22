class TemperatureConverter:

    def __init__(self):
        self.scale_factors = {'C': {'F': 9 / 5, 'K': 1}, 'F': {'C': 5 / 9, 'K': 5 / 9}, 'K': {'C': -273.15, 'F': -459.67}}

    def convert(self, value, from_scale, to_scale):
        if from_scale not in self.scale_factors or to_scale not in self.scale_factors[from_scale]:
            raise ValueError('Invalid scale')
        return value * self.scale_factors[from_scale][to_scale] + self.scale_factors[from_scale].get('K', 0)
if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_celsius = 25.0
    sample_fahrenheit = 77.0
    print(converter.convert(sample_celsius, 'C', 'F'))
    print(converter.convert(sample_fahrenheit, 'F', 'C'))
    print(converter.convert(293.15, 'K', 'C'))