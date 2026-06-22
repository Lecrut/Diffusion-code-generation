class Weight:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_kilograms(self):
        if self.unit == 'kg':
            return self.value
        if self.unit == 'lb':
            return self.value * 0.453592
        if self.unit == 'oz':
            return self.value * 0.0283495
        return self.value

    def convert_to(self, target_unit):
        if target_unit == self.unit:
            return self.value
        value_in_kg = self.to_kilograms()
        if target_unit == 'kg':
            return value_in_kg
        if target_unit == 'lb':
            return value_in_kg / 0.453592
        if target_unit == 'oz':
            return value_in_kg / 0.0283495
        return value_in_kg

    def set_unit(self, new_unit):
        if new_unit in ('kg', 'lb', 'oz'):
            self.unit = new_unit
        else:
            raise ValueError("Unsupported unit")

if __name__ == '__main__':
    w = Weight(100, 'lb')
    print(w.to_kilograms())
    print(w.convert_to('kg'))
    w.set_unit('kg')
    print(w.convert_to('lb'))