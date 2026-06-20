class Weight:
    def __init__(self, value, unit='kg'):
        self.value = value
        self.unit = unit

    def to_kg(self):
        if self.unit == 'kg':
            return self.value
        if self.unit == 'lb':
            return self.value * 0.45359237
        if self.unit == 'oz':
            return self.value * 0.0283495
        return self.value

    def convert(self, target_unit):
        kg = self.to_kg()
        if target_unit == 'kg':
            return kg
        if target_unit == 'lb':
            return kg / 0.45359237
        if target_unit == 'oz':
            return kg / 0.0283495
        return kg

    def set_unit(self, target_unit):
        kg = self.to_kg()
        if target_unit == 'kg':
            self.value = kg
        elif target_unit == 'lb':
            self.value = kg / 0.45359237
        elif target_unit == 'oz':
            self.value = kg / 0.0283495
        else:
            raise ValueError(f"Unsupported unit: {target_unit}")
        self.unit = target_unit

if __name__ == '__main__':
    w = Weight(100, 'lb')
    result = w.convert('kg')
    print(result)
    w.set_unit('kg')
    print(w.value, w.unit)