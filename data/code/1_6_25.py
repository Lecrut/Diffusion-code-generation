class WeightConverter:

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit

    @classmethod
    def convert_unit(cls, instance, new_unit):
        if instance.unit == 'pounds' and new_unit == 'kilograms':
            conversion_factor = 0.453592
            instance.weight *= conversion_factor
            instance.unit = new_unit
        elif instance.unit == 'kilograms' and new_unit == 'pounds':
            conversion_factor = 2.20462
            instance.weight *= conversion_factor
            instance.unit = new_unit
        else:
            raise ValueError('Unsupported unit conversion')

    def __str__(self):
        return f'{self.weight} {self.unit}'
if __name__ == '__main__':
    weight_in_pounds = WeightConverter(100, 'pounds')
    print(weight_in_pounds)
    WeightConverter.convert_unit(weight_in_pounds, 'kilograms')
    print(weight_in_pounds)
    weight_in_kilograms = WeightConverter(45.3592, 'kilograms')
    print(weight_in_kilograms)
    WeightConverter.convert_unit(weight_in_kilograms, 'pounds')
    print(weight_in_kilograms)