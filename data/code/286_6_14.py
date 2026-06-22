class LengthConverter:
    def __init__(self, value=0, unit='in'):
        self.value = value
        self.unit = unit

    def set_value(self, value):
        self.value = value

    def set_unit(self, unit):
        self.unit = unit

    def convert_to_km(self):
        if self.unit == 'km':
            return self.value
        elif self.unit == 'm':
            return self.value / 1000.0
        elif self.unit == 'cm':
            return self.value / 100000.0
        elif self.unit == 'in':
            return self.value * 0.0254
        elif self.unit == 'ft':
            return self.value * 0.03048
        else:
            raise ValueError(f"Unknown unit: {self.unit}")

if __name__ == '__main__':
    converter = LengthConverter(1, 'in')
    print(converter.convert_to_km())