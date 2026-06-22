class LengthConverter:
    CONVERSION_FACTORS = {'in': 0.0254, 'cm': 1, 'm': 100, 'km': 100000}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def convert_to(self, target_unit):
        if self.unit not in self.CONVERSION_FACTORS or target_unit not in self.CONVERSION_FACTORS:
            raise ValueError(f'Unknown unit: {self.unit}/{target_unit}')
        return self.value * self.CONVERSION_FACTORS[self.unit] / self.CONVERSION_FACTORS[target_unit]
if __name__ == '__main__':
    converter = LengthConverter(1, 'in')
    print(converter.convert_to('cm'))
    converter.set_value(36)
    print(converter.get_value())