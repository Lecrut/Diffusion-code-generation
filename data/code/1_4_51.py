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
            raise ValueError('Unsupported unit conversion')

    def update_weight(self, new_weight):
        self.weight = new_weight
if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    converted_weight_kg = weight_in_pounds.convert_to('kilograms')
    print(f'Weight in kilograms: {converted_weight_kg}')
    weight_in_kilograms = WeightConverter(68.039, 'kilograms')
    converted_weight_lb = weight_in_kilograms.convert_to('pounds')
    print(f'Weight in pounds: {converted_weight_lb}')
    weight_in_pounds.update_weight(200)
    updated_converted_weight_kg = weight_in_pounds.convert_to('kilograms')
    print(f'Updated weight in kilograms: {updated_converted_weight_kg}')