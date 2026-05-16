class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit
    def convert_weight(self, new_unit):
        if self.unit == new_unit:
            return self.weight
        elif self.unit == "pounds" and new_unit == "kilograms":
            conversion_factor = 0.453592
            new_weight = self.weight * conversion_factor
            self.unit = new_unit
            return new_weight
        elif self.unit == "kilograms" and new_unit == "pounds":
            conversion_factor = 2.204622
            new_weight = self.weight * conversion_factor
            self.unit = new_unit
            return new_weight
        else:
            return "Unsupported conversion"
if __name__ == '__main__':
    converter1 = WeightConverter(150, "pounds")
    print(f"Initial weight: {converter1.weight} {converter1.unit}")
    result1 = converter1.convert_weight("kilograms")
    print(f"Converted weight: {result1:.2f} {converter1.unit}")
    converter2 = WeightConverter(75, "kilograms")
    print(f"Initial weight: {converter2.weight} {converter2.unit}")
    result2 = converter2.convert_weight("pounds")
    print(f"Converted weight: {result2:.2f} {converter2.unit}")