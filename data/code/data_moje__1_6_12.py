class WeightConverter:
    CONVERSION_FACTORS = {
        'kg': 1.0,
        'lb': 2.20462,
        'g': 0.001,
        'oz': 35.274
    }

    def __init__(self, value, unit='kg'):
        unit = unit.lower()
        if unit not in self.CONVERSION_FACTORS:
            raise ValueError("Unsupported unit")
        self._value_in_kg = value / self.CONVERSION_FACTORS[unit]

    def change_unit(self, new_unit):
        new_unit = new_unit.lower()
        if new_unit not in self.CONVERSION_FACTORS:
            raise ValueError("Unsupported unit")
        self._unit = new_unit

    def get_value(self, unit=None):
        if unit is None:
            unit = self._unit
        unit = unit.lower()
        if unit not in self.CONVERSION_FACTORS:
            raise ValueError("Unsupported unit")
        return self._value_in_kg * self.CONVERSION_FACTORS[unit]

    @property
    def value(self):
        return self.get_value()

if __name__ == '__main__':
    w = WeightConverter(10, 'kg')
    print(w.value)
    w.change_unit('lb')
    print(w.value)
    w.change_unit('oz')
    print(w.value)