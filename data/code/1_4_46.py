class WeightConverter:

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, new_unit):
        new_unit = new_unit.lower()
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
    weight_converter = WeightConverter(150, 'pounds')
    print(weight_converter)
    weight_converter.convert_to('kilograms')
    print(weight_converter)