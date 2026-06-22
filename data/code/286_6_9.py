class LengthConverter:

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def set_unit(self, new_unit):
        self.unit = new_unit

    def get_unit(self):
        return self.unit

    def convert_to_km(self):
        if self.unit == 'km':
            return self.value
        elif self.unit == 'm':
            return self.value / 1000.0
        elif self.unit == 'cm':
            return self.value / 100000.0
        elif self.unit == 'mi':
            return self.value * 1.609344
        elif self.unit == 'in':
            return self.value * 0.0254
        else:
            raise ValueError(f'Unknown unit: {self.unit}')
if __name__ == '__main__':
    converter = LengthConverter(10, 'cm')
    print(converter.convert_to_km())
    converter.set_value(5)
    converter.set_unit('in')
    print(converter.convert_to_km())