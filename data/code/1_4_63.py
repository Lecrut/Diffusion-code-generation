class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, new_unit):
        if self.unit == 'pounds' and new_unit.lower() == 'kilograms':
            return self._convert_pounds_to_kilograms()
        elif self.unit == 'kilograms' and new_unit.lower() == 'pounds':
            return self._convert_kilograms_to_pounds()
        else:
            raise ValueError("Unsupported unit conversion")

    def _convert_pounds_to_kilograms(self):
        return self.weight * 0.453592

    def _convert_kilograms_to_pounds(self):
        return self.weight / 0.453592

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    converted_weight_kg = weight_in_pounds.convert_to('kilograms')
    print(f"Weight in kilograms: {converted_weight_kg}")

    weight_in_kilograms = WeightConverter(68.0389, 'kilograms')
    converted_weight_lb = weight_in_kilograms.convert_to('pounds')
    print(f"Weight in pounds: {converted_weight_lb}")