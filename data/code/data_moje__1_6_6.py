class Weight:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def change_unit(self, new_unit):
        if self.unit == new_unit:
            return
        if self.unit == 'lb' and new_unit == 'kg':
            self.value = self.value * 0.45359237
            self.unit = new_unit
        elif self.unit == 'kg' and new_unit == 'lb':
            self.value = self.value / 0.45359237
            self.unit = new_unit
        else:
            raise ValueError('Unsupported conversion')

    def get_weight(self):
        return self.value

if __name__ == '__main__':
    sample_weight = Weight(100, 'lb')
    print(sample_weight.get_weight())
    sample_weight.change_unit('kg')
    print(sample_weight.get_weight())
    sample_weight.change_unit('lb')
    print(sample_weight.get_weight())