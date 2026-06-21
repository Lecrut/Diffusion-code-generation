class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, target_unit):
        target_unit = target_unit.lower()
        if self.unit == 'pounds' and target_unit == 'kilograms':
            return self.weight * 0.453592
        elif self.unit == 'kilograms' and target_unit == 'pounds':
            return self.weight / 0.453592
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(100, 'pounds')
    print(f"Weight in kilograms: {weight_in_pounds.convert_to('kilograms')}")

    weight_in_kilograms = WeightConverter(45.3592, 'kilograms')
    print(f"Weight in pounds: {weight_in_kilograms.convert_to('pounds')}")