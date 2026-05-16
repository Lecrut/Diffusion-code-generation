class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit
    def convert_weight(self, new_unit):
        if self.unit == new_unit:
            return self.weight
        elif self.unit == "lbs" and new_unit == "kg":
            converted_weight = self.weight * 0.453592
            self.unit = "kg"
            return converted_weight
        elif self.unit == "kg" and new_unit == "lbs":
            converted_weight = self.weight / 0.453592
            self.unit = "lbs"
            return converted_weight
        else:
            return self.weight
if __name__ == '__main__':
    converter1 = WeightConverter(150, "lbs")
    print(f"Original weight: {converter1.weight} {converter1.unit}")
    result1 = converter1.convert_weight("kg")
    print(f"Converted weight: {result1} {converter1.unit}")
    converter2 = WeightConverter(75, "kg")
    print(f"Original weight: {converter2.weight} {converter2.unit}")
    result2 = converter2.convert_weight("lbs")
    print(f"Converted weight: {result2} {converter2.unit}")
    converter3 = WeightConverter(200, "lbs")
    print(f"Original weight: {converter3.weight} {converter3.unit}")
    result3 = converter3.convert_weight("lbs")
    print(f"No conversion needed: {result3} {converter3.unit}")