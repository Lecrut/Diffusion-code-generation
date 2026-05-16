class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit
    def convert_weight(self, new_unit):
        if self.unit == new_unit:
            return self.weight
        elif self.unit == "lb" and new_unit == "kg":
            converted_weight = self.weight * 0.453592
            self.unit = new_unit
            self.weight = converted_weight
            return converted_weight
        elif self.unit == "kg" and new_unit == "lb":
            converted_weight = self.weight / 0.453592
            self.unit = new_unit
            self.weight = converted_weight
            return converted_weight
        else:
            raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    converter1 = WeightConverter(150, "lb")
    print(f"Initial weight: {converter1.weight} {converter1.unit}")
    converted1 = converter1.convert_weight("kg")
    print(f"Converted weight: {converted1} {converter1.unit}")
    converter2 = WeightConverter(75, "kg")
    print(f"Initial weight: {converter2.weight} {converter2.unit}")
    converted2 = converter2.convert_weight("lb")
    print(f"Converted weight: {converted2} {converter2.unit}")