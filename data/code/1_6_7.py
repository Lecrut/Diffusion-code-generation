class Weight:
    def __init__(self, value: float, unit: str = "kg"):
        self._value = value
        self._unit = unit

    def to_kilograms(self) -> float:
        if self._unit == "kg":
            return self._value
        if self._unit == "lb":
            return self._value * 0.45359237
        return self._value

    def to_pounds(self) -> float:
        if self._unit == "lb":
            return self._value
        if self._unit == "kg":
            return self._value / 0.45359237
        return self._value

    def convert_to(self, new_unit: str) -> float:
        kg_value = self.to_kilograms()
        if new_unit == "kg":
            return kg_value
        if new_unit == "lb":
            return kg_value / 0.45359237
        return kg_value

if __name__ == '__main__':
    w = Weight(10, "lb")
    result = w.convert_to("kg")
    print(result)