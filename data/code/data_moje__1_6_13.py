class Weight:
    def __init__(self, value, unit="kg"):
        self.value = value
        self.unit = unit.lower()
        self._conversion_factors = {
            "kg": 1.0,
            "lbs": 0.453592,
            "g": 0.001,
            "oz": 0.0283495
        }

    def _to_kg(self):
        return self.value * self._conversion_factors[self.unit]

    def change_unit(self, new_unit):
        new_unit = new_unit.lower()
        if new_unit not in self._conversion_factors:
            raise ValueError("Unsupported unit")
        kg_value = self._to_kg()
        self.value = kg_value / self._conversion_factors[new_unit]
        self.unit = new_unit
        return self.value

    def __repr__(self):
        return f"{self.value} {self.unit}"

if __name__ == "__main__":
    weight = Weight(100, "lbs")
    print(weight)
    new_value = weight.change_unit("kg")
    print(new_value)
    print(weight)