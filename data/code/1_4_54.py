class WeightConverter:

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert_to(self, new_unit):
        if self.unit == 'pounds' and new_unit.lower() == 'kilograms':
            conversion_factor = 0.453592
            self.weight *= conversion_factor
            self.unit = 'kilograms'
        elif self.unit == 'kilograms' and new_unit.lower() == 'pounds':
            conversion_factor = 2.20462
            self.weight *= conversion_factor
            self.unit = 'pounds'
        else:
            raise ValueError('Unsupported unit conversion')

    def __str__(self):
        return f'{self.weight} {self.unit}'
if __name__ == '__main__':
    weight_converter = WeightConverter(100, 'Pounds')
    print(weight_converter)
    weight_converter.convert_to('Kilograms')
    print(weight_converter)
    weight_converter = WeightConverter(50, 'Kilograms')
    print(weight_converter)
    weight_converter.convert_to('Pounds')
    print(weight_converter)