class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit
    def convert_weight(self, new_unit):
        if self.unit == "pounds" and new_unit == "kilograms":
            conversion_factor = 0.453592
            self.weight = self.weight * conversion_factor
            self.unit = "kilograms"
        elif self.unit == "kilograms" and new_unit == "pounds":
            conversion_factor = 2.204622
            self.weight = self.weight * conversion_factor
            self.unit = "pounds"
        elif self.unit == new_unit:
            pass
        else:
            raise ValueError("Unsupported unit conversion.")
if __name__ == '__main__':
    converter1 = WeightConverter(150, "pounds")
    print(f"Initial weight: {converter1.weight} {converter1.unit}")
    converter1.convert_weight("kilograms")
    print(f"Converted weight: {converter1.weight} {converter1.unit}")
    converter2 = WeightConverter(75, "kilograms")
    print(f"Initial weight: {converter2.weight} {converter2.unit}")
    converter2.convert_weight("pounds")
    print(f"Converted weight: {converter2.weight} {converter2.unit}")
    converter3 = WeightConverter(100, "pounds")
    print(f"Initial weight: {converter3.weight} {converter3.unit}")
    try:
        converter3.convert_weight("furlongs")
    except ValueError as e:
        print(f"Error: {e}")