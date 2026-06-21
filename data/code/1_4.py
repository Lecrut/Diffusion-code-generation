class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, new_unit):
        if self.unit == 'pounds' and new_unit.lower() == 'kilograms':
            return self.weight * 0.453592
        elif self.unit == 'kilograms' and new_unit.lower() == 'pounds':
            return self.weight / 0.453592
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(100, 'pounds')
    converted_weight_kg = weight_in_pounds.convert_to('kilograms')
    print(f"Weight in kilograms: {converted_weight_kg}")

    weight_in_kg = WeightConverter(45.3592, 'kilograms')
    converted_weight_lb = weight_in_kg.convert_to('pounds')
    print(f"Weight in pounds: {converted_weight_lb}")