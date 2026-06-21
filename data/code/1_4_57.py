class WeightConverter:

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, target_unit):
        target_unit = target_unit.lower()
        if self.unit == target_unit:
            return self.weight
        conversion_factors = {'pounds': {'kilograms': 0.453592}, 'kilograms': {'pounds': 2.20462}}
        if self.unit not in conversion_factors or target_unit not in conversion_factors[self.unit]:
            raise ValueError(f'Conversion from {self.unit} to {target_unit} is not supported.')
        converted_weight = self.weight * conversion_factors[self.unit][target_unit]
        return converted_weight
if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    print(weight_in_pounds.convert_to('kilograms'))