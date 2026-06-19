class WeightConverter:

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, new_unit):
        if self.unit == 'pounds' and new_unit.lower() == 'kilograms':
            converted_weight = self.weight * 0.453592
        elif self.unit == 'kilograms' and new_unit.lower() == 'pounds':
            converted_weight = self.weight / 0.453592
        else:
            raise ValueError('Unsupported conversion unit')
        return WeightConverter(converted_weight, new_unit)

    def __repr__(self):
        return f'{self.weight} {self.unit}'
if __name__ == '__main__':
    weight_in_pounds = WeightConverter(100, 'pounds')
    print(weight_in_pounds)
    weight_in_kg = weight_in_pounds.convert_to('kilograms')
    print(weight_in_kg)