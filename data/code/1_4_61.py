class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, new_unit):
        if self.unit == 'pounds' and new_unit.lower() == 'kilograms':
            conversion_factor = 0.453592
        elif self.unit == 'kilograms' and new_unit.lower() == 'pounds':
            conversion_factor = 1 / 0.453592
        else:
            raise ValueError("Unsupported unit conversion")
        
        converted_weight = self.weight * conversion_factor
        return WeightConverter(converted_weight, new_unit)

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    converted_weight_kg = weight_in_pounds.convert_to('kilograms')
    print(f"Weight in kilograms: {converted_weight_kg.weight} {converted_weight_kg.unit}")

    weight_in_kilograms = WeightConverter(68.0389, 'kilograms')
    converted_weight_lb = weight_in_kilograms.convert_to('pounds')
    print(f"Weight in pounds: {converted_weight_lb.weight} {converted_weight_lb.unit}")