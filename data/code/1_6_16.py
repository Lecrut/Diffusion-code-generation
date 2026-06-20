class Weight:
    def __init__(self, value, unit="kg"):
        self.value = value
        self.unit = unit

    def convert(self, new_unit):
        if self.unit == new_unit:
            return self.value
        if self.unit == "kg" and new_unit == "lb":
            self.value = self.value * 2.20462
            self.unit = "lb"
        elif self.unit == "lb" and new_unit == "kg":
            self.value = self.value / 2.20462
            self.unit = "kg"
        elif self.unit == "g" and new_unit == "kg":
            self.value = self.value / 1000.0
            self.unit = "kg"
        elif self.unit == "kg" and new_unit == "g":
            self.value = self.value * 1000.0
            self.unit = "g"
        elif self.unit == "g" and new_unit == "lb":
            temp_kg = self.value / 1000.0
            self.value = temp_kg * 2.20462
            self.unit = "lb"
        elif self.unit == "lb" and new_unit == "g":
            temp_kg = self.value / 2.20462
            self.value = temp_kg * 1000.0
            self.unit = "g"
        else:
            raise ValueError(f"Unsupported conversion from {self.unit} to {new_unit}")
        return self.value

if __name__ == '__main__':
    weight = Weight(100, "kg")
    result = weight.convert("lb")
    print(result)