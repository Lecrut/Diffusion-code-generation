class WeightConverter:

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit.lower()

    def convert(self, new_unit):
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
    weight_obj = WeightConverter(10, 'pounds')
    print(weight_obj)
    weight_obj.convert('kilograms')
    print(weight_obj)