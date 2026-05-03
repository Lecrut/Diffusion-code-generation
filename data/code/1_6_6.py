class WeightConverter:
    def __init__(self):
        self.weight = 0.0
        self.unit = "lb"
    def set_weight(self, value, unit):
        self.weight = value
        self.unit = unit
    def convert_to_kg(self):
        if self.unit == "lb":
            return self.weight * 0.453592
        elif self.unit == "kg":
            return self.weight
        else:
            raise ValueError("Unsupported unit")
    def convert_to_lb(self):
        if self.unit == "lb":
            return self.weight
        elif self.unit == "kg":
            return self.weight / 0.453592
        else:
            raise ValueError("Unsupported unit")
if __name__ == '__main__':
    converter = WeightConverter()
    converter.set_weight(150, "lb")
    print(f"Original weight: {converter.weight} {converter.unit}")
    kg_value = converter.convert_to_kg()
    print(f"Converted weight in kg: {kg_value}")
    converter.set_weight(75, "kg")
    lb_value = converter.convert_to_lb()
    print(f"Converted weight in lb: {lb_value}")