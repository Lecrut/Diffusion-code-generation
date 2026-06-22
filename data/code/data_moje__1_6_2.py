class Weight:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convert(self, new_unit):
        if self.unit == new_unit:
            return self.value
        if self.unit == 'lb' and new_unit == 'kg':
            return self.value * 0.453592
        if self.unit == 'kg' and new_unit == 'lb':
            return self.value / 0.453592
        raise ValueError(f"Unsupported conversion from {self.unit} to {new_unit}")

if __name__ == '__main__':
    w = Weight(10, 'lb')
    print(w.convert('kg'))
    print(w.convert('lb'))
    w2 = Weight(5, 'kg')
    print(w2.convert('lb'))