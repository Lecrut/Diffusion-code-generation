class Weight:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def change_unit(self, new_unit):
        if self.unit == "lbs" and new_unit == "kg":
            return Weight(self.value * 0.453592, "kg")
        elif self.unit == "kg" and new_unit == "lbs":
            return Weight(self.value * 2.20462, "lbs")
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == "__main__":
    initial_weight = Weight(150, "lbs")
    converted_weight = initial_weight.change_unit("kg")
    print(converted_weight.value)
    print(converted_weight.unit)