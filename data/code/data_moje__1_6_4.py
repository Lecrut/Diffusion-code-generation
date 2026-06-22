class Weight:
    def __init__(self, value, unit="pounds"):
        self.value = value
        self.unit = unit

    def to_kilograms(self):
        if self.unit == "pounds":
            return self.value * 0.453592
        elif self.unit == "kilograms":
            return self.value
        else:
            raise ValueError("Unsupported unit for conversion to kilograms")

    def convert(self, target_unit):
        if target_unit == self.unit:
            return self
        if self.unit == "pounds" and target_unit == "kilograms":
            new_value = self.value * 0.453592
            self.value = new_value
            self.unit = target_unit
        elif self.unit == "kilograms" and target_unit == "pounds":
            new_value = self.value / 0.453592
            self.value = new_value
            self.unit = target_unit
        else:
            raise ValueError("Unsupported conversion")
        return self

if __name__ == '__main__':
    w = Weight(10, "pounds")
    w.convert("kilograms")
    print(w.value, w.unit)