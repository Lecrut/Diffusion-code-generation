class LengthConverter:

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convert_to_cm(self):
        if self.unit == 'in':
            return self.value * 2.54
        elif self.unit == 'cm':
            return self.value
        else:
            raise ValueError(f'Unknown unit for conversion: {self.unit}')

    def convert_to_in(self):
        if self.unit == 'in':
            return self.value
        elif self.unit == 'cm':
            return self.value / 2.54
        else:
            raise ValueError(f'Unknown unit for conversion: {self.unit}')
if __name__ == '__main__':
    converter = LengthConverter(10, 'cm')
    print(converter.convert_to_in())
    converter.value = 5
    converter.unit = 'in'
    print(converter.convert_to_cm())