class Weight:
    def __init__(self, value, unit='kg'):
        self.value = value
        self.unit = unit

    def to_kg(self):
        if self.unit == 'kg':
            return self.value
        if self.unit == 'lb':
            return self.value * 0.453592
        if self.unit == 'oz':
            return self.value * 0.0283495
        return self.value

    def set_unit(self, new_unit):
        if new_unit == self.unit:
            return
        current_kg = self.to_kg()
        if new_unit == 'kg':
            self.value = current_kg
        elif new_unit == 'lb':
            self.value = current_kg / 0.453592
        elif new_unit == 'oz':
            self.value = current_kg / 0.0283495
        else:
            raise ValueError(f"Unsupported unit: {new_unit}")
        self.unit = new_unit

    def get_display_value(self):
        return f"{self.value:.4f} {self.unit}"

if __name__ == '__main__':
    w = Weight(100, 'lb')
    print(w.get_display_value())
    w.set_unit('kg')
    print(w.get_display_value())
    w.set_unit('oz')
    print(w.get_display_value())