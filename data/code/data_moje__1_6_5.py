class Weight:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def change_unit(self, new_unit):
        if self.unit == "lb" and new_unit == "kg":
            self.value = self.value * 0.453592
            self.unit = "kg"
        elif self.unit == "kg" and new_unit == "lb":
            self.value = self.value * 2.20462
            self.unit = "lb"
        else:
            raise ValueError("Unsupported unit conversion")
        return self.value, self.unit

if __name__ == '__main__':
    sample_weight = Weight(10, "lb")
    result_value, result_unit = sample_weight.change_unit("kg")
    print(f"{result_value} {result_unit}")
    sample_weight.change_unit("lb")
    result_value, result_unit = sample_weight.change_unit("kg")
    print(f"{result_value} {result_unit}")