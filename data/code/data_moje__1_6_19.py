class WeightConverter:
    CONVERSION_FACTORS = {
        'kg': 1.0,
        'lb': 2.20462,
        'g': 0.001,
        'oz': 35.274
    }

    def __init__(self, value, unit='kg'):
        if unit not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {unit}")
        self._unit = unit
        self._value = value

    def get_value(self):
        return self._value

    def get_unit(self):
        return self._unit

    def change_unit(self, new_unit):
        if new_unit not in self.CONVERSION_FACTORS:
            raise ValueError(f"Unsupported unit: {new_unit}")
        
        current_factor = self.CONVERSION_FACTORS[self._unit]
        new_factor = self.CONVERSION_FACTORS[new_unit]
        
        normalized_value = self._value / current_factor
        self._value = normalized_value * new_factor
        self._unit = new_unit

    def __repr__(self):
        return f"{self._value:.4f} {self._unit}"

if __name__ == '__main__':
    weight = WeightConverter(150, 'lb')
    print(weight)
    weight.change_unit('kg')
    print(weight)
    weight.change_unit('oz')
    print(weight)
    weight.change_unit('g')
    print(weight)