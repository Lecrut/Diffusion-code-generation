class WeightConverter:
    def __init__(self):
        self.weight = 0.0
        self.unit = "lb"
    def set_weight(self, value, unit):
        self.weight = value
        self.unit = unit
    def convert_weight(self, target_unit):
        if self.unit == target_unit:
            return self.weight
        elif self.unit == "lb" and target_unit == "kg":
            return self.weight * 0.453592
        elif self.unit == "kg" and target_unit == "lb":
            return self.weight / 0.453592
        else:
            raise ValueError("Unsupported unit conversion")
if __name__ == '__main__':
    converter = WeightConverter()
    converter.set_weight(150, "lb")
    print(f"Original weight: {converter.weight} {converter.unit}")
    kg_weight = converter.convert_weight("kg")
    print(f"Converted weight to kg: {kg_weight:.2f} kg")
    lb_weight = converter.convert_weight("lb")
    print(f"Converted weight to lb: {lb_weight:.2f} lb")