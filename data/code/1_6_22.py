class WeightConverter:

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit

    def convert_to(self, new_unit):
        if self.unit == 'pounds' and new_unit == 'kilograms':
            conversion_factor = 0.453592
            self.weight *= conversion_factor
            self.unit = new_unit
        elif self.unit == 'kilograms' and new_unit == 'pounds':
            conversion_factor = 2.20462
            self.weight *= conversion_factor
            self.unit = new_unit
        else:
            raise ValueError('Unsupported unit conversion')

    def __str__(self):
        return f'{self.weight} {self.unit}'
if __name__ == '__main__':
    weight_in_pounds = WeightConverter(150, 'pounds')
    print(weight_in_pounds)
    weight_in_pounds.convert_to('kilograms')
    print(weight_in_pounds)
    weight_in_kilograms = WeightConverter(70, 'kilograms')
    print(weight_in_kilograms)
    weight_in_kilograms.convert_to('pounds')
    print(weight_in_kilograms)