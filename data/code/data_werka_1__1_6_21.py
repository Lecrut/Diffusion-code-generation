class WeightConverter:

    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit

    @classmethod
    def convert_unit(cls, instance, new_unit):
        if instance.unit == 'pounds' and new_unit == 'kilograms':
            instance.weight *= 0.453592
            instance.unit = new_unit
        elif instance.unit == 'kilograms' and new_unit == 'pounds':
            instance.weight /= 0.453592
            instance.unit = new_unit
        else:
            raise ValueError('Unsupported unit conversion')

    def __str__(self):
        return f'{self.weight} {self.unit}'
if __name__ == '__main__':
    weight_instance = WeightConverter(100, 'pounds')
    print(weight_instance)
    WeightConverter.convert_unit(weight_instance, 'kilograms')
    print(weight_instance)