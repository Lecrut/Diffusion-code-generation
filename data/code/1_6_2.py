class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
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
    weight_pounds = 150.0
    unit_pounds = "lb"
    converter = WeightConverter(weight_pounds, unit_pounds)
    print(f"Original weight: {weight_pounds} {unit_pounds}")
    weight_kilograms = converter.convert_weight("kg")
    print(f"Converted weight: {weight_kilograms:.2f} kg")
    weight_pounds_back = converter.convert_weight("lb")
    print(f"Converted weight back to pounds: {weight_pounds_back:.2f} lb")