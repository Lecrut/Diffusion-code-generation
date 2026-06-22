class WeightContainer:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convert_to(self, new_unit):
        if self.unit == new_unit:
            return self.value
        
        kg = self._to_kg(self.value, self.unit)
        result = self._from_kg(kg, new_unit)
        self.unit = new_unit
        return result

    def _to_kg(self, value, unit):
        if unit == 'kg':
            return value
        if unit == 'lb':
            return value * 0.453592
        if unit == 'oz':
            return value * 0.0283495
        if unit == 'g':
            return value * 0.001
        raise ValueError(f"Unsupported unit: {unit}")

    def _from_kg(self, kg_value, unit):
        if unit == 'kg':
            return kg_value
        if unit == 'lb':
            return kg_value / 0.453592
        if unit == 'oz':
            return kg_value / 0.0283495
        if unit == 'g':
            return kg_value * 1000
        raise ValueError(f"Unsupported target unit: {unit}")

if __name__ == '__main__':
    weight = WeightContainer(10, 'lb')
    converted_weight = weight.convert_to('kg')
    print(converted_weight)