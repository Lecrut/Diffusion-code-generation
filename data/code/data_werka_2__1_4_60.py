class WeightConverter:
    POUNDS_TO_KILOGRAMS = 0.453592
    KILOGRAMS_TO_POUNDS = 1 / POUNDS_TO_KILOGRAMS

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, new_unit):
        if self.unit == 'pounds' and new_unit.lower() == 'kilograms':
            return self.weight * self.POUNDS_TO_KILOGRAMS
        elif self.unit == 'kilograms' and new_unit.lower() == 'pounds':
            return self.weight * self.KILOGRAMS_TO_POUNDS
        else:
            raise ValueError("Unsupported unit conversion")

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(200, 'pounds')
    converted_weight_kg = weight_in_pounds.convert_to('kilograms')
    print(f"Weight in kilograms: {converted_weight_kg}")

    weight_in_kilograms = WeightConverter(90.7185, 'kilograms')
    converted_weight_lb = weight_in_kilograms.convert_to('pounds')
    print(f"Weight in pounds: {converted_weight_lb}")