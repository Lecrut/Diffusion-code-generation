class WeightConverter:
    def __init__(self, value, unit='lbs'):
        self._value = float(value)
        self._unit = unit.lower()
        self._units = {'lbs': 1.0, 'kg': 0.453592}

    def convert(self, new_unit):
        new_unit = new_unit.lower()
        if new_unit not in self._units:
            raise ValueError(f"Unsupported unit: {new_unit}")
        value_in_lbs = self._value / self._units[self._unit]
        self._value = value_in_lbs * self._units[new_unit]
        self._unit = new_unit

    def get_weight(self):
        return self._value, self._unit

if __name__ == '__main__':
    w = WeightConverter(150, 'lbs')
    w.convert('kg')
    print(w.get_weight())
    w2 = WeightConverter(70, 'kg')
    w2.convert('lbs')
    print(w2.get_weight())